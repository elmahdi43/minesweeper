import settings
import random
import sys
import ctypes
from tkinter import Button, Label


class Cell:
    all = []
    cell_count_label_object = None
    count= settings.CELL_COUNT
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_condidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location,
                     width=settings.CELL_WIDTH,
                     height=settings.CELL_HEIGHT,

                     )
        # trigger right clic and left clic            )
        btn.bind('<Button-1>', self.left_click_actions )
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axies(self.x - 1, self.y - 1),
            self.get_cell_by_axies(self.x, self.y - 1),
            self.get_cell_by_axies(self.x + 1, self.y - 1),
            self.get_cell_by_axies(self.x - 1, self.y),
            self.get_cell_by_axies(self.x - 1, self.y + 1),
            self.get_cell_by_axies(self.x, self.y + 1),
            self.get_cell_by_axies(self.x + 1, self.y),
            self.get_cell_by_axies(self.x + 1, self.y + 1),
        ]
        # print(surrounded_cells)
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        m = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                m += 1
        return m

    def left_click_actions(self, event):
        # We will check if the cell is mine or not.
        if self.is_mine :
            self.show_mine()
        else :
            if self.surrounded_cells_mines_length == 0 :
                for cell_obj in self.surrounded_cells :
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.count==settings.MINES_COUNT:

                ctypes.windll.user32.MessageBoxW(0, 'You win !', 'Game over', 0)

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-1>')

    def get_cell_by_axies(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y :
                return cell
    # Mined cells logic.
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0 , 'You clicked on a mine', 'Game over', 0)
        sys.exit()


    # Unmined cells logic.

    def show_cell(self):
        if not self.is_opened :

            Cell.count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            if Cell.cell_count_label_object :
                Cell.cell_count_label_object.configure(
                    text=f"Cells left: {Cell.count}"
                )
            self.cell_btn_object.configure(
                bg="SystemButtonFace",
            )
        self.is_opened = True
    def right_click_actions(self, event):
        if not self.is_mine_condidate :
            self.cell_btn_object.configure(
                bg="orange",
            )

        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace',
            )
            self.is_mine_condidate = False
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells left: {settings.CELL_COUNT}",
            width=12,
            height=4,
            background="green",
            fg="white",
            font=("", 30 )

        )
        Cell.cell_count_label_object = lbl


    @staticmethod

    def Randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT

        )

        for picked_cell in picked_cells :
            picked_cell.is_mine= True



    def __repr__(self):
        return f"Cell({self.x},{self.y})"
