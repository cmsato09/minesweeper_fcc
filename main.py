from tkinter import Tk, Frame, Button, Label
import settings
from cell import Cell

root_window = Tk()  # initiates window

# Window setting configurations
root_window.configure(bg="gray")
root_window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # Width x Height
root_window.title('Minesweeper')  # changes title of the window from default 'tk'
root_window.resizable(False, False)

top_frame = Frame(
    root_window,
    bg='black',
    width=settings.WIDTH,
    height=settings.height_percent(10),
)
top_frame.place(x=0, y=0)

title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='MineSweeper',
    font=('', 14),
    )
title.place(x=settings.width_percent(30), y=0)

center_frame = Frame(
        root_window,
        bg='purple',
        width=settings.width_percent(75),
        height=settings.height_percent(75),
    )
center_frame.place(
    x=0,
    y=settings.height_percent(10),
)


def create_field():
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


create_field()


def reset_game():
    for cell in Cell.all_cells:
        cell.is_opened = False
        cell.is_mine = False
        cell.is_mine_candidate = False
        cell.cell_button_obj.configure(
            text="",
            bg="SystemButtonFace",
        )
        cell.cell_button_obj.bind('<Button-1>', cell.left_click_action)
        cell.cell_button_obj.bind('<Button-3>', cell.right_click_action)
    Cell.cell_count = settings.CELL_COUNT - settings.MINE_NUMBER
    Cell.mine_count = settings.MINE_NUMBER
    Cell.cell_count_label_object.configure(
        text=f"Cells Left: {Cell.cell_count}\n"
             f"Flags Left: {Cell.mine_count}",
    )
    Cell.randomize_mines()


reset_button = Button(
    top_frame,
    text="reset",
    command=reset_game,
)
reset_button.place(x=300, y=10)


# Runs the window until exit button is pressed
root_window.mainloop()
