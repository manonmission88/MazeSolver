
from tkinter import Tk, BOTH,Canvas
class Window:
    def __init__(self,width,height):
        self.height = height 
        self.width = width 
        self._root = Tk()
        self._root.title('Maze Solver')
        self.canvas = Canvas(self._root,width = self.width, height = self.height,bg='white')
        self.canvas.pack(fill=BOTH, expand = True)
        self._running = False 
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._running = True 
        while self._running:
            self.redraw()
    
    def close(self):
        self._running = False 
        self._root.destroy()

if __name__ == '__main__':
    window = Window(800,600)
    window.wait_for_close()
    
            
        
    
    