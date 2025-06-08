import tkinter as tk
from constants import WINDOW_SIZE, WINDOW_MARGIN


def draw_points(grid_size, points, lines):
    root = tk.Tk()
    root.title("Point Drawing")
    root.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

    canvas = tk.Canvas(root, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1], bg="white")
    canvas.pack()

    for x, y in lines:
        if (x, y) in points:
            continue
        rel_x = round((x / grid_size[0]) * WINDOW_SIZE[0])
        rel_y = round((y / grid_size[1]) * WINDOW_SIZE[1])
        canvas.create_oval(
            rel_x - 2, rel_y - 2, rel_x + 2, rel_y + 2, fill="black", outline="black"
        )

    for x, y in points:
        rel_x = round((x / grid_size[0]) * WINDOW_SIZE[0])
        rel_y = round((y / grid_size[1]) * WINDOW_SIZE[1])
        canvas.create_oval(
            rel_x - 2, rel_y - 2, rel_x + 2, rel_y + 2, fill="red", outline="red"
        )

    root.mainloop()
