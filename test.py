from graphics import Window
from maze import Maze

win = Window(800, 600)
m = Maze(0, 0, 1, 12, 10, 10, win)

win.wait_for_close()
