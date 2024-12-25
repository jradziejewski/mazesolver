from graphics import Window
from maze import Maze

win = Window(800, 600)
m = Maze(50, 50, 5, 12, 50, 50, win)


win.wait_for_close()
