import csv
from pathlib import Path
from pyarrow import csv as pyarrow_csv
import pyarrow as pa

if __name__ == "__main__":
    schema = pa.schema(
        [
            ("bin_name", pa.string()),
            ("quantity", pa.int8()),
            ("keywords", pa.string()),
            ("height", pa.float64()),
            ("width", pa.float64()),
            ("material", pa.string()),
            ("color", pa.string()),
            ("accent", pa.string()),
            ("notes", pa.string()),
        ]
    )

    bin_names = []
    quantities = []
    keywords = []
    heights = []
    widths = []
    materials = []
    colors = []
    accents = []
    notes = []
    csv_path = Path("mysig_cookie_cutters_sheet1_v2.csv")
    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            # Row Number
            if i == 0:
                continue

            # Bin Name
            bin_name = " ".join(row[0].splitlines()).replace("  ", " ")
            bin_names.append(bin_name)

            # Description
            desc = " ".join(row[2].splitlines()).replace("/", ",").replace("  ", " ")
            note = " ".join(row[7].splitlines()).replace("/", ",").replace("  ", " ")
            quantity = 1
            if len(desc) > 3 and desc[-3] == "(" and desc[-1] == ")":
                quantity = desc[-2]
                desc = desc[:-3]
            keywords.append(desc)
            notes.append(note)
            quantities.append(int(quantity))

            # Material
            if row[3]:
                materials.append(row[3])
            else:
                materials.append("NONE")

            # Color
            accent = "NONE"
            color = " ".join(row[4].splitlines()).replace("  ", " ")
            if color and "W/" in color:
                color, accent = color.split(" W/ ")
                accent_parts = accent.split()
                if len(accent_parts) == 4:
                    accent = " ".join(accent.split()[0:2])
                else:
                    accent = accent_parts[0]
            colors.append(color)
            accents.append(accent)

            # Height and Width
            height, width = (
                row[5]
                .replace("APPROX.", "")
                .replace("EACH", "")
                .replace('"X', '" X')
                .replace('"', "")
                .replace(",", ".")
                .split(" X ")
            )
            height, width = float(height.strip()), float(width.strip())
            heights.append(height)
            widths.append(width)

    table = pa.table(
        [
            bin_names,
            quantities,
            keywords,
            heights,
            widths,
            materials,
            colors,
            accents,
            notes,
        ],
        schema=schema,
    )

    pyarrow_csv.write_csv(table, "mysig_cookie_cutter_sheet1_v3.csv")
    print(table)
    print(f"num rows: {table.num_rows}")
