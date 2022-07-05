
#
WIDTH = 384
HEIGHT = 462
GRID_SIZE_X = 16
GRID_SIZE_Y = 16
CELL_COUNT = GRID_SIZE_X * GRID_SIZE_Y
MINE_NUMBER = CELL_COUNT // 5 - 11


def width_percent(percentage):
    return WIDTH / 100 * percentage


def height_percent(percentage):
    return HEIGHT / 100 * percentage
