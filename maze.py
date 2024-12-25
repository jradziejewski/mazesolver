from graphics import Point
from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.__win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for _ in range(0, self.num_rows):
            row = []
            for _ in range(0, self.num_cols):
                row.append(Cell(self.__win))
            self._cells.append(row)

        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        p1 = Point(
            self._x1 + i * self._cell_size_x,
            self._y1 + j * self._cell_size_y
        )
        p2 = Point(
            p1.x + self._cell_size_x,
            p1.y + self._cell_size_y
        )

        self._cells[i][j].draw(p1, p2)
        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)
