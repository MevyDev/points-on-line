import random


def rejection_sampling(x_size, y_size, point_count):
    points_used = set()

    while len(points_used) != point_count:
        x = random.randint(0, x_size - 1)
        y = random.randint(0, y_size - 1)
        points_used.add((x, y))

    return list(points_used)


def reservior_sampling(x_size, y_size, point_count):
    possible = []
    for x in range(0, x_size):
        for y in range(0, y_size):
            possible.append((x, y))
    random.shuffle(possible)
    return possible[:point_count]


def generate_input(x_size, y_size, point_count):
    max_points = x_size * y_size
    if point_count <= max_points * 0.5:
        return rejection_sampling(x_size, y_size, point_count)
    return reservior_sampling(x_size, y_size, point_count)
