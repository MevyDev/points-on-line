import random


def main():
    points_used = set()
    max_x = int(input("Enter the max X value: "))
    max_y = int(input("Enter the max Y value: "))

    point_count = int(input("Enter the amount of points: "))

    for i in range(point_count):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        points_used.add((x, y))

    for point in points_used:
        print(f"{point[0]} {point[1]}")


if __name__ == "__main__":
    main()
