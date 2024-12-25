from graphics import Window
from maze import Maze

win = Window(800, 600)
m = Maze(0, 0, 5, 5, 10, 10, win)

win.wait_for_close()
