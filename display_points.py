import tkinter as tk
from constants import WINDOW_SIZE, WINDOW_MARGIN


def draw_points(grid_size, points, lines):
    ratio = grid_size[0] / grid_size[1]
    ratio = max(ratio, grid_size[1] / grid_size[0])

    if grid_size[0] > grid_size[1]:
        x_window = WINDOW_SIZE
        y_window = round(WINDOW_SIZE / ratio)
    else:
        x_window = round(WINDOW_SIZE / ratio)
        y_window = WINDOW_SIZE

    root = tk.Tk()
    root.title("Point Drawing")
    geometry_string = f"{x_window + WINDOW_MARGIN * 2}x{y_window + WINDOW_MARGIN * 2}"
    root.geometry(geometry_string)

    canvas = tk.Canvas(
        root,
        width=x_window + WINDOW_MARGIN * 2,
        height=y_window + WINDOW_MARGIN * 2,
        bg="white",
    )
    canvas.pack()

    radius = max(1, (min(x_window // grid_size[0], y_window // grid_size[1])) // 2)

    for x, y in lines:
        rel_x = round((x / grid_size[0]) * x_window) + WINDOW_MARGIN
        rel_y = round((y / grid_size[1]) * y_window) + WINDOW_MARGIN
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
