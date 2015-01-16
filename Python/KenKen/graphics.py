from Tkinter import *

class Animation():
    def __init__(self, rows = 6, cols = 6):
        self.rows = rows
        self.cols = cols

        self.height = 60 * rows
        self.width = 60 * cols

        self.grid = [["#0000FF"] * cols for i in xrange(rows)]

        self.root = Tk()
        self.canvas = Canvas(self.root, height = self.height, width = self.width)
        self.canvas.pack()

        self.root.bind("<Button-1>", self.highlight)
        self.root.bind("<B1-Motion>", self.highlight)
        self.root.bind("<Shift-Button-1>", self.depress)
        self.root.bind("<Shift-B1-Motion>", self.depress)

        self.redrawAll()    
        self.root.mainloop()

    def redrawAll(self):
        self.canvas.delete(ALL)
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                color = self.grid[row][col]
                self.canvas.create_rectangle(60 * col, 60 * row, 60 * col + 60, 60 * row + 60, fill = color, outline = "white")

    def highlight(self, event):
        row = event.y / 60
        col = event.x / 60

        try: self.grid[row][col] = "#8888FF"
        except: pass

        self.redrawAll()

    def depress(self, event):
        row = event.y / 60
        col = event.x / 60

        try: self.grid[row][col] = "#0000FF"
        except: pass

        self.redrawAll()

Animation(5, 4)