from tkinter import Tk, Frame, Button, Label, Menu
import settings
from cell import Cell

root_window = Tk()  # initiates window

top_frame = Frame(
    root_window,
    bg='black',
    width=settings.WIDTH,
    height=settings.height_percent(15),
)
center_frame = Frame(
    root_window,
    bg='purple',
    width=settings.width_percent(75),
    height=settings.height_percent(75),
)

DIFFICULTY_STATE = 'Beginner'

difficulty = {
    'Beginner': {
        'WIDTH': 216,
        'HEIGHT': 280,
        'GRID_SIZE_X': 9,
        'GRID_SIZE_Y': 9,
        'MINES': 10,
    },
    'Intermediate': {
        'WIDTH': 384,
        'HEIGHT': 462,
        'GRID_SIZE_X': 16,
        'GRID_SIZE_Y': 16,
        'MINES': 40,
    },
    'Advanced': {
        'WIDTH': 720,
        'HEIGHT': 462,
        'GRID_SIZE_X': 30,
        'GRID_SIZE_Y': 16,
        'MINES': 99,
    },
}


def create_window(w, h):
    # Window setting configurations
    root_window.configure(bg="gray")
    root_window.geometry(f'{w}x{h}')
    root_window.title('Minesweeper')
    root_window.resizable(False, False)

    # Menu
    menu_bar = Menu(root_window)
    root_window.configure(menu=menu_bar)
    difficulty_menu = Menu(menu_bar)
    menu_bar.add_cascade(label="Difficulty", menu=difficulty_menu)
    difficulty_menu.add_radiobutton(
        label="Beginner",
        value="Beginner",
        command=lambda value="Beginner": set_difficulty(value),
    )
    difficulty_menu.add_radiobutton(
        label="Intermediate",
        value="Advanced",
        command=lambda value="Intermediate": set_difficulty(value),
    )
    difficulty_menu.add_radiobutton(
        label="Advanced",
        value="Advanced",
        command=lambda value="Advanced": set_difficulty(value),
    )

    top_frame.place(x=0, y=0)

    # title = Label(
    #     top_frame,
    #     bg='black',
    #     fg='white',
    #     text='MineSweeper',
    #     font=('', 14),
    # )
    # title.place(x=width_percent(30), y=0)

    center_frame.place(
        x=0,
        y=settings.height_percent(16),
    )

    reset_button = Button(
        top_frame,
        text="reset",
        command=reset_game,
    )
    reset_button.place(x=settings.width_percent(75), y=10)


def create_field(difficulty_level):
    """
    Creates all cells and cell buttons based on grid size. Places all buttons
    in center play frame.
    Creates cell count and flag count label in top left of the frame.
    Randomize which cells are mines from created cells.
    """
    for x in range(difficulty[difficulty_level]['GRID_SIZE_X']):
        for y in range(difficulty[difficulty_level]['GRID_SIZE_Y']):
            c = Cell(x, y)
            c.create_button_obj(center_frame)
            c.cell_button_obj.grid(
                column=x, row=y,
            )

    Cell.create_cell_count_label(top_frame)
    Cell.cell_count_label_object.place(x=0, y=0)

    Cell.randomize_mines(difficulty[DIFFICULTY_STATE]['MINES'])


def set_difficulty(difficulty_level):
    """
    Depending on the difficulty, the window resizes itself, the label, and
    number of buttons
    """
    global DIFFICULTY_STATE
    DIFFICULTY_STATE = difficulty_level

    root_window.geometry(
        f"{difficulty[difficulty_level]['WIDTH']}x{difficulty[difficulty_level]['HEIGHT']}"
    )
    top_frame.configure(
        width=difficulty[difficulty_level]['WIDTH'],
        height=difficulty[difficulty_level]['HEIGHT'],
    )
    Cell.cell_count = difficulty[difficulty_level]['GRID_SIZE_X'] * difficulty[difficulty_level]['GRID_SIZE_Y']
    Cell.mine_count = difficulty[difficulty_level]['MINES']
    Cell.update_count()

    for child in center_frame.winfo_children():
        child.destroy()
    Cell.all_cells = []
    Cell.cell_count_label_object.destroy()
    create_field(difficulty_level)


def reset_game():
    """
    Resets game by setting all cells back to default position (cell is
    unopened, not a mine, not flagged). Cell button is set to unopened (no
    text) and back to default color.
    Cell count and flag count label is set to full count.
    Re-picks cell for mines after everything is set back to default.
    Considering it uses everything from the Cell class, is it better to put
    this function in cell.py?
    """
    global DIFFICULTY_STATE
    for cell in Cell.all_cells:
        cell.is_opened = False
        cell.is_mine = False
        cell.is_mine_candidate = False
        cell.cell_button_obj.configure(
            text="",
            bg="SystemButtonFace",
            relief="raised"
        )
        cell.cell_button_obj.bind('<ButtonRelease-1>', cell.left_click_action)
        cell.cell_button_obj.bind('<Button-3>', cell.right_click_action)
    Cell.cell_count = difficulty[DIFFICULTY_STATE]['GRID_SIZE_X'] * \
                      difficulty[DIFFICULTY_STATE]['GRID_SIZE_Y']
    Cell.mine_count = difficulty[DIFFICULTY_STATE]['MINES']
    Cell.cell_count_label_object.configure(
        text=f"Cells Left: {Cell.cell_count}\n"
             f"Flags Left: {Cell.mine_count}",
    )
    Cell.randomize_mines(difficulty[DIFFICULTY_STATE]['MINES'])


def main():
    create_window(settings.WIDTH, settings.HEIGHT)
    create_field(DIFFICULTY_STATE)
    root_window.mainloop()


if __name__ == "__main__":
    main()
