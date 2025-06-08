def main():
    lines = []
    best = 0
    points = []
    with open("input.txt", "r") as f:
        for line in f:
            coords = line.split(" ")
            lines.append((coords[0], coords[1]))

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
        if best < len(mp[cur_best]):
            best = len(mp[cur_best])
            points = mp[cur_best].copy()

    print(f"targets hit: {best}")
    print(f"target list: {points}")


if __name__ == "__main__":
    main()
