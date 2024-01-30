import csv
from collections import Counter
from pathlib import Path
import plotly.graph_objects as go


def plot_heights(heights_x: list[float], heights_y: list[int]):
    fig = go.Figure(
        data=[
            go.Bar(
                x=heights_x,
                y=heights_y,
                text=heights_y,
                textposition="auto",
                width=0.25,
            )
        ]
    )
    fig.update_layout(
        title_text="Cookie Cutter Height Distribution",
        xaxis=dict(
            title="Height (inches)",
        ),
        yaxis=dict(
            title="Count",
        ),
    )
    fig.show()


def plot_widths(widths_x: list[float], widths_y: list[int]):
    fig = go.Figure(
        data=[
            go.Bar(
                x=widths_x,
                y=widths_y,
                text=widths_y,
                textposition="auto",
                width=0.25,
            )
        ]
    )
    fig.update_layout(
        title_text="Cookie Cutter Width Distribution",
        xaxis=dict(
            title="Width (inches)",
        ),
        yaxis=dict(
            title="Count",
        ),
    )
    fig.show()


if __name__ == "__main__":
    csv_path = Path("./Mysig Cookie Cutters - Sheet1.csv")

    bin_names = []
    materials = []
    accents = []
    colors = []
    heights_list = []
    widths_list = []
    seq_count = 0
    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            # Row Number
            if i == 0:
                continue

            # Bin Name
            bin_name = " ".join(row[0].splitlines()).replace("  ", " ")
            if bin_name:
                bin_names.append(bin_name)
            else:
                bin_names.append("NONE")

            # Bin and Sequence Count
            if row[1]:
                seq_count += 1

            # Description
            desc = " ".join(row[2].splitlines()).replace("/", ",").replace("  ", " ")
            notes = " ".join(row[7].splitlines()).replace("/", ",").replace("  ", " ")
            quantity = 1
            if len(desc) > 3 and desc[-3] == "(" and desc[-1] == ")":
                quantity = desc[-2]
                desc = desc[:-3]

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
            accents.append(accent)
            colors.append(color)

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
            heights_list.append(height)
            widths_list.append(width)

            print(f"CSV Row: {i+1}")
            print(f"Bin Name: {bin_name}")
            print(f"Quantity: {quantity}")
            print(f"Keywords: {desc}, {notes}")
            print(f"Height: {height}")
            print(f"Width: {width}")
            print(f"Material: {row[3]}")
            print(f"Color: {color}")
            print(f"Accent: {accent}\n")

            # Picture

            # Notes

    bin_counter = Counter(bin_names)
    print(f"\ncolors ({len(bin_counter)}, {sum(bin_counter.values())}):")
    for bin, count in sorted(bin_counter.items()):
        print(f"\t{bin}  ({count})")

    materials_counter = Counter(materials)
    print(f"\nmaterials ({len(materials_counter)}, {sum(materials_counter.values())}):")
    for mat, count in sorted(materials_counter.items()):
        print(f"\t{mat}  ({count})")

    colors_counter = Counter(colors)
    print(f"\ncolors ({len(colors_counter)}, {sum(colors_counter.values())}):")
    for color, count in sorted(colors_counter.items()):
        print(f"\t{color}  ({count})")

    accents_counter = Counter(accents)
    print(f"\naccents ({len(accents_counter)}, {sum(accents_counter.values())}):")
    for accent, count in sorted(accents_counter.items()):
        print(f"\t{accent}  ({count})")

    heights_x = []
    heights_y = []
    heights_counter = Counter(heights_list)
    print(f"\nheights ({len(heights_counter)}, {sum(heights_counter.values())}):")
    for height, count in sorted(heights_counter.items()):
        heights_x.append(height)
        heights_y.append(count)
        print(f"\t{height:5}  ({count:3})")

    widths_x = []
    widths_y = []
    widths_counter = Counter(widths_list)
    print(f"\nwidths ({len(widths_counter)}, {sum(widths_counter.values())}):")
    for width, count in sorted(widths_counter.items()):
        widths_x.append(width)
        widths_y.append(count)
        print(f"\t{width:5}  ({count:3})")

    print(f"\nbin and sequence count: {seq_count}")

    # plot_heights(heights_x, heights_y)
    # plot_widths(widths_x, widths_y)
