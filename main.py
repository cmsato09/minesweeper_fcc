import tkinter as tk
import settings
from cell import Cell

root = tk.Tk()  # initiates window

# Window setting configurations
root.configure(bg="gray")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # Width x Height
root.title('Minesweeper')  # changes title of the window from default 'tk'
root.resizable(False, False)

top_frame = tk.Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=settings.height_percent(10),
)
top_frame.place(x=0, y=0)

title = tk.Label(
    top_frame,
    bg='black',
    fg='white',
    text='MineSweeper',
    font=('', 14),
    )
title.place(x=settings.width_percent(30), y=0)

center_frame = tk.Frame(
    root,
    bg='purple',
    width=settings.width_percent(75),
    height=settings.height_percent(75),
)
center_frame.place(
    x=0,
    y=settings.height_percent(10),
)

# grid in center frame
for x in range(settings.GRID_SIZE_X):
    for y in range(settings.GRID_SIZE_Y):
        c = Cell(x, y)
        c.create_button_obj(center_frame)
        c.cell_button_obj.grid(
            column=x, row=y,
        )

Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


# Runs the window until exit button is pressed
root.mainloop()
