
#
WIDTH = 720
HEIGHT = 480
GRID_SIZE = 6
CELL_COUNT = GRID_SIZE ** 2
MINE_COUNT = CELL_COUNT // 4


def width_percent(percentage):
    return WIDTH / 100 * percentage


def height_percent(percentage):
    return HEIGHT / 100 * percentage
