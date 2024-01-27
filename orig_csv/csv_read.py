import csv
from collections import Counter
from pathlib import Path


if __name__ == "__main__":
    csv_path = Path("./Mysig Cookie Cutters - Sheet1.csv")

    bin_names = set()
    materials = set()
    colors = set()
    heights_list = []
    widths_list = []
    seq_count = 0
    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            # Row Number
            if i == 0:
                continue
            print(f"CSV Row: {i+1}")

            # Bin Name
            bin_name = " ".join(row[0].splitlines()).replace("  ", " ")
            bin_names.add(bin_name)
            print(f"Bin Name: {bin_name}")

            # Bin and Sequence Count
            if row[1]:
                seq_count += 1

            # Description
            desc = " ".join(row[2].splitlines()).replace("/", ",").replace("  ", " ")
            notes = " ".join(row[7].splitlines()).replace("/", ",").replace("  ", " ")
            print(f"Keywords: {desc}, {notes}")

            # Material
            if row[3]:
                materials.add(row[3])
            print(f"Material: {row[3]}")

            # Color
            color = " ".join(row[4].splitlines()).replace("  ", " ")
            colors.add(color)
            print(f"Color: {color}")

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

            print(f"Height: {height}")
            print(f"Width: {width}\n")

            # Picture

            # Notes

    print(f"bin names ({len(bin_names)}):")
    for name in sorted(list(bin_names)):
        if name:
            print(f"\t{name}")

    print(f"\nmaterials ({len(materials)}):")
    for mat in sorted(list(materials)):
        if mat:
            print(f"\t{mat}")

    print(f"\ncolors ({len(colors)}):")
    for color in sorted(list(colors)):
        if color:
            print(f"\t{color}")

    heights_counter = Counter(heights_list)
    print(f"\nheights ({len(heights_counter)}):")
    for height, count in sorted(heights_counter.items()):
        print(f"\t{height:5}  ({count:3})")

    widths_counter = Counter(widths_list)
    print(f"\nwidths ({len(widths_counter)}):")
    for width, count in sorted(widths_counter.items()):
        print(f"\t{width:5}  ({count:3})")

    print(f"\nbin and sequence count: {seq_count}")
