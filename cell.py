from window import Line, Point

class Cell:
    def __init__(self,win=None):
        self.has_left_wall = True 
        self.has_right_wall = True 
        self.has_top_wall = True  
        self.has_bottom_wall = True 
        self._x1 = None
        self._x2 = None 
        self._y1 = None
        self._y2 = None
        self._win = win 
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        color = "#d9d9d9"  # background color
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, color)

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, color)

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, color)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))  # <-- FIXED THIS LINE
            self._win.draw_line(line, color)

    # helper function to find the center of the two walls
    def get_center(self):
        x_center = abs((self._x1 + self._x2) / 2)
        y_center = abs((self._y1 + self._y2) / 2)
        return x_center, y_center

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        x1, y1 = self.get_center()
        x2, y2 = to_cell.get_center()

        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, color)





