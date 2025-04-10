
from tkinter import Tk, BOTH,Canvas

"""
    A class to create and manage a graphical window using Tkinter for a Maze Solver application.
    Attributes:
        width (int): The width of the window.
        height (int): The height of the window.
        canvas (Canvas): The Tkinter Canvas widget used for drawing.
        _root (Tk): The root Tkinter window.
        _running (bool): A flag to indicate whether the window is running.
    Constructor:
        __init__(width, height):
            Initializes the Window object with the specified width and height.
 """ 
class Window:
    def __init__(self,width,height):
        self.height = height 
        self.width = width 
        self._root = Tk()
        self._root.title('Maze Solver')
        self.canvas = Canvas(self._root,width = self.width, height = self.height,bg='white')
        self.canvas.pack()
        self._running = False 
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    # close the window 
    def wait_for_close(self):
        self._running = True 
        while self._running:
            self.redraw()
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

         
    def close(self):
        self._running = False 


#draw point - should have x and y points 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1 
        self.point2 = point2 
    
    def draw(self, canvas, fill_color = 'black'):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y, 
            fill=fill_color, width=2
        )
        



    
        
    
    
            
        
    
    