import time
import random
from cell import Cell
from PIL import Image

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

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self, animate=False):
        """Create a 2D grid of Cell objects (row-major)."""
        self._cells = [
            [Cell(self._win) for _ in range(self._num_cols)]
            for _ in range(self._num_rows)
        ]
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col, animate=animate)

    def _draw_cell(self, row, col, animate=False):
        if self._win is None:
            return
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[row][col].draw(x1, y1, x2, y2)
        if animate:
            self._animate()

    def _capture_frame(self, frame_list):
        if self._win and hasattr(self._win, 'canvas'):
            self._win.canvas.update()
            self._win.canvas.postscript(file="frame.eps")
            img = Image.open("frame.eps").convert("RGB")
            frame_list.append(img)

    def _animate(self, frame_list=None):
        if self._win is not None:
            self._win.redraw()
            if frame_list is not None:
                self._capture_frame(frame_list)
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def is_valid(self, r, c):
        return 0 <= r < self._num_rows and 0 <= c < self._num_cols

    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if self.is_valid(new_r, new_c) and not self._cells[new_r][new_c].visited:
                if dr == 1:
                    self._cells[row][col].has_bottom_wall = False
                    self._cells[new_r][new_c].has_top_wall = False
                elif dr == -1:
                    self._cells[row][col].has_top_wall = False
                    self._cells[new_r][new_c].has_bottom_wall = False
                elif dc == 1:
                    self._cells[row][col].has_right_wall = False
                    self._cells[new_r][new_c].has_left_wall = False
                elif dc == -1:
                    self._cells[row][col].has_left_wall = False
                    self._cells[new_r][new_c].has_right_wall = False

                self._draw_cell(row, col, animate=True)
                self._break_walls_r(new_r, new_c)

        self._draw_cell(row, col, animate=True)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, r, c):
        self._animate()
        curr_cell = self._cells[r][c]
        curr_cell.visited = True

        if r == self._num_rows - 1 and c == self._num_cols - 1:
            return True

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + dr
            new_c = c + dc

            if not self.is_valid(new_r, new_c):
                continue

            next_cell = self._cells[new_r][new_c]
            if next_cell.visited:
                continue

            if dr == 1 and curr_cell.has_bottom_wall:
                continue
            if dr == -1 and curr_cell.has_top_wall:
                continue
            if dc == 1 and curr_cell.has_right_wall:
                continue
            if dc == -1 and curr_cell.has_left_wall:
                continue

            curr_cell.draw_move(next_cell)
            if self._solve_r(new_r, new_c):
                return True
            curr_cell.draw_move(next_cell, undo=True)

        return False

    def solve(self):
        self._reset_cells_visited()
        solved = self._solve_r(0, 0)
        if solved:
            self._show_solved_message()
        return solved

    def _show_solved_message(self):
        if self._win is not None and hasattr(self._win, 'canvas'):
            self._win.canvas.create_text(
                self._x1 + self._num_cols * self._cell_size_x // 2,
                self._y1 + self._num_rows * self._cell_size_y + 20,
                text="Maze Solved ✅",
                fill="green",
                font=("Helvetica", 16, "bold")
            )
