import tkinter as tk


def draw_points(window_size, grid_size, points, lines):
    root = tk.Tk()
    root.title("Point Drawing")
    root.geometry(f"{window_size[0]}x{window_size[1]}")

    canvas = tk.Canvas(root, width=window_size[0], height=window_size[1], bg="white")
    canvas.pack()

    for x, y in lines:
        if (x, y) in points:
            continue
        rel_x = round((x / grid_size[0]) * window_size[0])
        rel_y = round((y / grid_size[1]) * window_size[1])
        canvas.create_oval(
            rel_x - 2, rel_y - 2, rel_x + 2, rel_y + 2, fill="black", outline="black"
        )

    for x, y in points:
        rel_x = round((x / grid_size[0]) * window_size[0])
        rel_y = round((y / grid_size[1]) * window_size[1])
        canvas.create_oval(
            rel_x - 2, rel_y - 2, rel_x + 2, rel_y + 2, fill="red", outline="red"
        )

    root.mainloop()
