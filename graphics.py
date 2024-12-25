from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__root.protocol("MY_DELETE_WINDOW", self.close)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running is True:
            self.redraw()

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__window = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, p1, p2):
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y

        if self.has_left_wall:
            line = Line(p1, Point(p1.x, p2.y))
            self.__window.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(p2.x, p1.y), p2)
            self.__window.draw_line(line)
        if self.has_top_wall:
            line = Line(p1, Point(p2.x, p1.y))
            self.__window.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(p1.x, p2.y), p2)
            self.__window.draw_line(line)
