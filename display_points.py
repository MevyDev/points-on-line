import tkinter as tk
from constants import WINDOW_SIZE


def draw_points(grid_size, points, lines):
    grid_size_x, grid_size_y = grid_size[0] - 1, grid_size[1] - 1

    ratio = grid_size_x / grid_size_y
    ratio = max(ratio, grid_size_y / grid_size_x)

    if grid_size_x > grid_size_y:
        x_window = WINDOW_SIZE
        y_window = round(WINDOW_SIZE / ratio)
    else:
        x_window = round(WINDOW_SIZE / ratio)
        y_window = WINDOW_SIZE

    radius = max(1, (min(x_window // grid_size_x, y_window // grid_size_y)) // 2)
    window_margin = radius

    root = tk.Tk()
    root.title("Point Drawing")
    geometry_string = f"{x_window + window_margin * 2}x{y_window + window_margin * 2}"
    root.geometry(geometry_string)

    canvas = tk.Canvas(
        root,
        width=x_window + window_margin * 2,
        height=y_window + window_margin * 2,
        bg="white",
    )
    canvas.pack()

    first_x = round((points[0][0] / grid_size_x) * x_window) + window_margin
    first_y = round((points[0][1] / grid_size_y) * y_window) + window_margin
    for x, y in points:
        rel_x = round((x / grid_size_x) * x_window) + window_margin
        rel_y = round((y / grid_size_y) * y_window) + window_margin
        canvas.create_line(rel_x, rel_y, first_x, first_y, fill="blue", width=2)

    for x, y in lines:
        rel_x = round((x / grid_size_x) * x_window) + window_margin
        rel_y = round((y / grid_size_y) * y_window) + window_margin
        if (x, y) in points:
            canvas.create_oval(
                rel_x - radius,
                rel_y - radius,
                rel_x + radius,
                rel_y + radius,
                fill="red",
                outline="red",
            )
            continue
        canvas.create_oval(
            rel_x - radius,
            rel_y - radius,
            rel_x + radius,
            rel_y + radius,
            fill="black",
            outline="black",
        )

    root.mainloop()
