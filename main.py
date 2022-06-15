from tkinter import *
import settings
from cell import Cell

root = Tk()  # initiate window

# Window setting configurations
root.configure(bg="gray")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # Width x Height
root.title('Minesweeper')  # changes title of the window from default 'tk'
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='blue',
    width=settings.WIDTH,
    height=settings.height_percent(25),
)
top_frame.place(x=0, y=0)

title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='MineSweeper',
    font=('', 30),
    )
title.place(x=settings.width_percent(25), y=0)


left_sideframe = Frame(
    root,
    bg='black',
    width=settings.width_percent(25),
    height=settings.height_percent(75),
)
left_sideframe.place(x=0, y=settings.height_percent(25))

center_frame = Frame(
    root,
    bg='purple',
    width=settings.width_percent(75),
    height=settings.height_percent(75),
)
center_frame.place(
    x=settings.width_percent(25),
    y=settings.height_percent(25),
)

# grid in center frame
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_obj(center_frame)
        c.cell_button_obj.grid(
            column=x, row=y,
        )

Cell.create_cell_count_label(left_sideframe)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


# Runs the window until exit button is pressed
root.mainloop()
