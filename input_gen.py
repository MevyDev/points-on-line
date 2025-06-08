import random


def generate_input(x_size, y_size, point_count):
    points_used = set()

    for i in range(point_count):
        x = random.randint(0, x_size)
        y = random.randint(0, y_size)
        points_used.add((x, y))

    return list(points_used)
