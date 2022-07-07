# Minesweeper tutorial project

## Project Description

This is a minesweeper game made using Python's Tkinter following a tutorial 
posted by [freeCodeCamp](https://www.freecodecamp.org/news/object-oriented-programming-with-python-code-a-minesweeper-game/), 
originally by [JimShapedCoding](https://www.youtube.com/watch?v=OqbGRZx4xUc)

This tutorial covers object-oriented programming by creating a class for a 
"cell" in minesweeper. By left-clicking or right-clicking a cell, a cell will 
open to show the number of surrounding mines or a mine, or be flagged as a 
potential mine. The number of cells left and flags left is tracked.  

This tutorial also covers the algorithm associated with displaying the number
of mines surrounding a particular cell, open surrounding cells if the 
surrounding cells has no mines, and randomizing mine placement.
The basics of tkinter is touched upon, but not expanded. 

Other features not covered by the freeCodeCamp tutorial was googled
(looked at Tkinter tutorial pages, stackoverflow to see if others had problems 
implementing certain Tkinter features, watched other youtube videos, etc.).

## How to Install

1. Clone this Github project
2. Make sure you have cell.py, main.py, and settings.py downloaded

## How to Play

Run the main.py file to play the game. It will open a Tkinter window. Start 
clicking on cells!

### Changelog
v1.2 -- Added reset button. Reset the game any time or after winning or losing.
Cells become flat after being pressed to differentiate between opened and 
unopened.

v1.1 -- Fixed surrounding cell bug where only surrounding cells were opened 
when a cell had zero mines around. Recursively opens surrounding cells so if 
there are other zero mine cells next to zero mine cells, it opens.

v1.0 -- Coded base game covered in tutorial