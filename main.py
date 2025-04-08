from window import Window, Point, Line
from cell import cell

def main():
    win = Window(800,600)
    
    cell = cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = cell(win)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = cell(win)
    cell.has_bottom_wall = False
    cell.draw(225, 225, 250, 250)

    cell = cell(win)
    cell.has_top_wall = False
    cell.draw(300, 300, 500, 500)

    win.wait_for_cell()


main()
