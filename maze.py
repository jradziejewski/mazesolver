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
        win=None,
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
        self._break_entrance_and_exit()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _create_cells(self):
        for _ in range(0, self.num_cols):
            row = []
            for _ in range(0, self.num_rows):
                row.append(Cell(self.__win))
            self._cells.append(row)

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.__win is None:
            return
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
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)
