import tkinter as tk
from constants import WINDOW_SIZE, WINDOW_MARGIN


def draw_points(grid_size, points, lines):
    root = tk.Tk()
    root.title("Point Drawing")
    root.geometry(
        f"{WINDOW_SIZE[0] + WINDOW_MARGIN * 2}x{WINDOW_SIZE[1] + WINDOW_MARGIN * 2}"
    )

    canvas = tk.Canvas(
        root,
        width=WINDOW_SIZE[0] + WINDOW_MARGIN * 2,
        height=WINDOW_SIZE[1] + WINDOW_MARGIN * 2,
        bg="white",
    )
    canvas.pack()

    radius = max(
        1, (min(WINDOW_SIZE[0] // grid_size[0], WINDOW_SIZE[1] // grid_size[1])) // 2
    )

    for x, y in lines:
        rel_x = round((x / grid_size[0]) * WINDOW_SIZE[0]) + WINDOW_MARGIN
        rel_y = round((y / grid_size[1]) * WINDOW_SIZE[1]) + WINDOW_MARGIN
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
