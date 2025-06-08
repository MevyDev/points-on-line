from input_gen import generate_input
from display_points import draw_points
from constants import INPUT_FILE


def update_input(x_size, y_size, point_count, input_file):
    lines = generate_input(x_size, y_size, point_count)
    with open(input_file, "w") as f:
        f.write(f"{x_size} {y_size}\n")
        for line in lines:
            f.write(f"{line[0]} {line[1]}\n")
    return


def solve(lines):
    points = []
    best = 0
    for line in lines:
        x1 = int(line[0])
        y1 = int(line[1])
        mp = {}
        for com_line in lines:
            x2 = int(com_line[0])
            y2 = int(com_line[1])

            if x1 == x2 and y1 == y2:
                continue

            if x2 - x1 == 0:
                angle = float("inf")
            else:
                angle = (y2 - y1) / (x2 - x1)

            if angle not in mp:
                mp[angle] = [(x2, y2)]
            else:
                mp[angle].append((x2, y2))

        cur_best = None
        for ang in mp:
            if cur_best is None:
                cur_best = ang
            elif len(mp[ang]) > len(mp[cur_best]):
                cur_best = ang
        mp[cur_best].append((x1, y1))
        if best < len(mp[cur_best]):
            best = len(mp[cur_best])
            points = mp[cur_best].copy()
    return points


def main():
    choice = input("Enter 'u' to update the input file: ")
    if choice.strip().lower() == "u":
        x_size = int(input("Enter the size of the grid on the X axis: "))
        y_size = int(input("Enter the size of the grid on the Y axis: "))
        point_count = int(input("Enter the point count: "))
        update_input(x_size, y_size, point_count, INPUT_FILE)

    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            coords = line.split(" ")
            lines.append((int(coords[0]), int(coords[1])))

    x_size = int(lines[0][0])
    y_size = int(lines[0][1])

    points = solve(lines[1:])
    best = len(points)

    print(f"grid size x: {x_size}")
    print(f"grid size Y: {y_size}")
    print(f"targets hit: {best}")
    print(f"target list: {points}")

    draw_points((x_size, y_size), points, lines[1:])


if __name__ == "__main__":
    main()
