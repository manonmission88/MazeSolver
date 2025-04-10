import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self.seed = seed
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self, animate=False):
        """Create a 2D grid of Cell objects in row-major order."""
        self._cells = [
            [Cell(self._win) for _ in range(self._num_cols)]
            for _ in range(self._num_rows)
        ]
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col, animate=animate)

    def _draw_cell(self, row, col, animate=False):
        """Draw the cell at (row, col)."""
        if self._win is None:
            return
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[row][col].draw(x1, y1, x2, y2)
        if animate:
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        """Open the top wall at entrance and bottom wall at exit."""
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, row, col):
        """Recursive backtracking algorithm to generate the maze."""

        def is_valid(r, c):
            return (
                0 <= r < self._num_rows
                and 0 <= c < self._num_cols
                and not self._cells[r][c].visited
            )

        self._cells[row][col].visited = True

        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]  # down, right, left, up
        random.shuffle(directions)

        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if is_valid(new_r, new_c):
                # Break walls between current cell and next
                if dr == 1:  # down
                    self._cells[row][col].has_bottom_wall = False
                    self._cells[new_r][new_c].has_top_wall = False
                elif dr == -1:  # up
                    self._cells[row][col].has_top_wall = False
                    self._cells[new_r][new_c].has_bottom_wall = False
                elif dc == 1:  # right
                    self._cells[row][col].has_right_wall = False
                    self._cells[new_r][new_c].has_left_wall = False
                elif dc == -1:  # left
                    self._cells[row][col].has_left_wall = False
                    self._cells[new_r][new_c].has_right_wall = False

                self._draw_cell(row, col, animate=True)
                self._break_walls_r(new_r, new_c)

        self._draw_cell(row, col, animate=True)
