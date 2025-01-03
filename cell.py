from graphics import Point, Line


class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.__window = win

        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw_move(self, to_cell, undo=False):
        if self.__window is None:
            return

        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_center = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )
        line = Line(self_center, to_center)
        if undo:
            self.__window.draw_line(line, "gray")
        else:
            self.__window.draw_line(line, "red")

    def draw(self, p1, p2):
        if self.__window is None:
            return

        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y

        line = Line(p1, Point(p1.x, p2.y))
        if self.has_left_wall:
            self.__window.draw_line(line)
        else:
            self.__window.draw_line(line, "black")

        line = Line(Point(p2.x, p1.y), p2)
        if self.has_right_wall:
            self.__window.draw_line(line)
        else:
            self.__window.draw_line(line, "black")

        line = Line(p1, Point(p2.x, p1.y))
        if self.has_top_wall:
            self.__window.draw_line(line)
        else:
            self.__window.draw_line(line, "black")

        line = Line(Point(p1.x, p2.y), p2)
        if self.has_bottom_wall:
            self.__window.draw_line(line)
        else:
            self.__window.draw_line(line, "black")
