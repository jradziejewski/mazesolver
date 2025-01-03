import time
import random
from graphics import Point
from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        if seed is None:
            self._seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self):
        return self._solve_dfs_r(0, 0)

    def _solve_dfs_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if (i == self.num_cols - 1) and (j == self.num_rows - 1):
            return True

        # left
        if i > 0 and (not self._cells[i][j].has_left_wall):
            left_cell = self._cells[i - 1][j]
            if not left_cell.visited:
                self._cells[i][j].draw_move(left_cell)
                if self._solve_dfs_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(left_cell, True)

            # right
        if i < self.num_cols - 1 and not self._cells[i][j].has_right_wall:
            right_cell = self._cells[i + 1][j]
            if not right_cell.visited:
                self._cells[i][j].draw_move(right_cell)
                if self._solve_dfs_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(right_cell, True)
        # top
        if j > 0 and (not self._cells[i][j].has_top_wall):
            bottom_cell = self._cells[i][j - 1]
            if not bottom_cell.visited:
                self._cells[i][j].draw_move(bottom_cell)
                if self._solve_dfs_r(i, j - 1) is True:
                    return True
                else:
                    self._cells[i][j].draw_move(bottom_cell, True)

            # bottom
        if j < self.num_rows - 1 and (not self._cells[i][j].has_bottom_wall):
            top_cell = self._cells[i][j + 1]
            if not top_cell.visited:
                self._cells[i][j].draw_move(top_cell)
                if self._solve_dfs_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(top_cell, True)


        return False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # bottom
            if j < self.num_rows - 1:
                top_cell = self._cells[i][j + 1]
                if not top_cell.visited:
                    to_visit.append((i, j + 1))

            # right
            if i < self.num_cols - 1:
                right_cell = self._cells[i + 1][j]
                if not right_cell.visited:
                    to_visit.append((i + 1, j))

            # top
            if j > 0:
                bottom_cell = self._cells[i][j - 1]
                if not bottom_cell.visited:
                    to_visit.append((i, j - 1))
            # left
            if i > 0:
                left_cell = self._cells[i - 1][j]
                if not left_cell.visited:
                    to_visit.append((i - 1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction_idx = random.randrange(0, len(to_visit))
            next_index = to_visit[direction_idx]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

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
        p1 = Point(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y)
        p2 = Point(p1.x + self._cell_size_x, p1.y + self._cell_size_y)

        self._cells[i][j].draw(p1, p2)
        self._animate()

    def _animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.000001)
