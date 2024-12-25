from graphics import Window
from maze import Maze


def main():
    win = Window(1200, 900)
    m = Maze(00, 00, 45, 45, 15, 15, win)
    m.solve()
    
    win.wait_for_close()

main()
