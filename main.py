from tkinter import *
from cell import Cell
import settings
import utils

board = Tk(screenName="Minesweeper")
board.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
board.title("Minesweeper")
board.resizable(False, False)
board.configure(
    bg="green"
)
top_frame = Frame(
    board,
    bg="red",
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(
    x=0,
    y=0
)

title_game = Label(
    top_frame,
    text="Minesweeper Game",
    font=('',48)

)
title_game.place(
    x=utils.width_prct(25),
    y=0
)
left_frame = Frame(
    board,
    bg='blue',
    width=utils.width_prct(30),
    height=utils.height_prct(75)
)
left_frame.place(
    x=0,
    y=utils.height_prct(25)
)

cell_frame = Frame(
    board,
    bg="white",
    width=utils.width_prct(70),
    height=utils.height_prct(75)
)
cell_frame.place(
    x=utils.width_prct(30),
    y=utils.height_prct(25)
)
# Instantiate our class
for i in range(settings.GRID_SIZE):
    for j in range(settings.GRID_SIZE):
        c1 = Cell(i,j)
        c1.create_btn_object(cell_frame)

        c1.cell_btn_object.grid(column=i, row=j)



#

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
# Test aria

Cell.Randomize_mines()
#for i in Cell.all:
#    print(i.is_mine)
# Run the Board
board.mainloop()

# Press Shift+F10 to execute it or replace it with your code
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
