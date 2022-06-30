from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all_cells = []
    cell_count = settings.CELL_COUNT - settings.MINE_NUMBER
    cell_count_label_object = None
    mine_count = settings.MINE_NUMBER
    text_color = {
        0: "white",
        1: "blue",
        2: "green",
        3: "red",
        4: "purple",
        5: "maroon",
        6: "turquoise",
        7: "black",
        8: "gray",
    }

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
            width=2,
            height=1,
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
            text=f"Cells Left: {Cell.cell_count}\n"
                 f"Flags Left: {settings.MINE_NUMBER}",
            font=('', 10),
        )
        Cell.cell_count_label_object = label

    def left_click_action(self, event):
        """When button is left-clicked, """
        # tkinter convention to have one more parameter to assign something to an event
        if self.is_mine:
            self.show_mine()
        else:
            self.show_surrounding_cells()
            self.show_cell()

            # If mines count is equal to the cells left count, player wins
            if Cell.cell_count == settings.MINE_NUMBER:
                ctypes.windll.user32.MessageBoxW(0, 'YOU WIN', 'WIN', 0)



    def right_click_action(self, event):
        """ When button is right-clicked, the button is flagged as a possible
            mine. The background of the button switches to yellow and flag
            count is decreased by 1. When button is already flagged, it reverts
            to the default color and flag count is increased by 1."""

        if not self.is_mine_candidate:
            self.cell_button_obj.configure(
                bg='yellow'
            )
            self.is_mine_candidate = True
            Cell.mine_count -= 1

            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}\n"
                         f"Flags Left: {Cell.mine_count}",
                )
        else:
            self.cell_button_obj.configure(
                bg='SystemButtonFace',
            )
            self.is_mine_candidate = False
            Cell.mine_count += 1

            #TODO make new function for updating cell and mine count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}\n"
                         f"Flags Left: {Cell.mine_count}",
                )

    def get_cell(self, x, y):
        # Return cell object based on x, y grid coordinates
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
        """ Displays number of mines surrounding cell when cell is opened. """
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(
                text=f"{self.surrounding_cells_mine_number}",
                fg=f"{Cell.text_color[self.surrounding_cells_mine_number]}",
            )
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}\n"
                         f"Flags Left: {Cell.mine_count}",
                )
            # If mine candidate, we should still be able to click it and the
            # button configures back to SystemButtonFace
            self.cell_button_obj.configure(bg='SystemButtonFace')
        self.is_opened = True
        # Cancel click events if button is opened
        self.cell_button_obj.unbind('<Button-1>')
        self.cell_button_obj.unbind('<Button-3>')

    def show_surrounding_cells(self):
        """ Opens surrounding cells if cell with zero surrounding mines is
            opened """
        if self.surrounding_cells_mine_number == 0:
            for cell_obj in self.surrounding_cells:
                if not cell_obj.is_opened:
                    cell_obj.show_cell()
                    cell_obj.is_opened = True
                    cell_obj.show_surrounding_cells()

    def show_mine(self):
        """ When a mine button is shown, the background turns red."""
        self.cell_button_obj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'MINE, BOOM', 'GAME OVER', 0)
        # sys.exit()  # exits game, TODO restart the game when you lose

    @staticmethod
    def randomize_mines():
        """ Randomly selects cells to become mines and number of mines depends
            on grid size and mine number """

        selected_cells = random.sample(Cell.all_cells, settings.MINE_NUMBER)
        for picked_cell in selected_cells:
            picked_cell.is_mine = True
