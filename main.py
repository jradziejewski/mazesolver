from graphics import Cell, Point, Line, Window


def main():
    w = Window(800, 600)
    c = Cell(w)
    c.draw(Point(00, 00), Point(100, 100))
    w.wait_for_close()


main()
