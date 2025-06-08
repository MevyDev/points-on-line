import random


def generate_input(max_x, max_y):
    points_used = set()

    point_count = int(input("Enter the amount of points: "))

    for i in range(point_count):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        points_used.add((x, y))

    return list(points_used)
