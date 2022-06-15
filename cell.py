from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all_cells = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_button_obj = None
        self.x = x
        self.y = y

        Cell.all_cells.append(self)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def create_button_obj(self, location):
        btn = Button(
            location,  # place button in a Frame()
            width=8,
            height=3,
        )
        btn.bind('<Button-1>', self.left_click_action)  # left-click. NOT calling method, REFERENCING method
        btn.bind('<Button-3>', self.right_click_action)  # right-click
        self.cell_button_obj = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            font=('', 14),
        )
        Cell.cell_count_label_object = label

    def left_click_action(self, event):
        # tkinter convention to have one more parameter to assign something to an event
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mine_number == 0:
                # shows surrounding cell if clicked cell has no surrounding mines
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
                    cell_obj.is_opened = True
            self.show_cell()

            # If mines count is equal to the cells left count, player wins
            if Cell.cell_count == settings.MINE_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'YOU WIN', 'WIN', 0)

        # Cancel click events if cell is already opened
        # TODO still able to right click if opened by surrounding cell = 0
        self.cell_button_obj.unbind('<Button-1>')
        self.cell_button_obj.unbind('<Button-3>')

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_button_obj.configure(
                bg='yellow'
            )
            self.is_mine_candidate = True
        else:
            self.cell_button_obj.configure(
                bg='SystemButtonFace',
            )
            self.is_mine_candidate = False

    def get_cell(self, x, y):
        # Return cell object based on x, y coordinate
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells_around_clicked = [
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1),
            self.get_cell(self.x, self.y + 1),
        ]
        cells_around_clicked = [cell for cell in cells_around_clicked if
                                cell is not None]
        return cells_around_clicked

    @property
    def surrounding_cells_mine_number(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        """display number of mines surrounding cell"""
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(
                text=f"{self.surrounding_cells_mine_number}"
            )
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}",
                )
            # If mine candidate, we should still be able to click it and the
            # button configures back to SystemButtonFace
            self.cell_button_obj.configure(bg='SystemButtonFace')
        self.is_opened = True

    def show_mine(self):
        # display "you lost" message
        self.cell_button_obj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'MINE, BOOM', 'GAME OVER', 0)
        sys.exit()  # exits game, TODO restart the game when you lose

    @staticmethod
    def randomize_mines():
        selected_cells = random.sample(Cell.all_cells, settings.MINE_COUNT)
        for picked_cell in selected_cells:
            picked_cell.is_mine = True
