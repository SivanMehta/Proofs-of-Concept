#####################################################################################################
## This animation was made to demonstrate the optical illusion that objects moving vertically look ##
## like they're moving faster than objects moving horizontally when they have the same speed.      ##
#####################################################################################################


from Tkinter import *

class Animation():
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 500, height = 500)
        self.canvas.pack()
        self.cx1, self.cy1 = 25, 75
        self.cx2, self.cy2 = 75, 25
        self.direction = 1

        self.draw()
        
        self.root.mainloop()

    def draw(self):
        self.canvas.delete(ALL)

        self.drawCircle(self.cx1, self.cy1, 1)
        self.drawCircle(self.cx2, self.cy2, 2)

        if(self.cx1 >= 475 or self.cx1 < 25):
            self.direction *= -1

        self.cx1 += 1 * self.direction
        self.cy2 += 1 * self.direction

        self.canvas.after(5, self.draw)

    def drawCircle(self, cx, cy, circleNumber):
        color = "blue" if circleNumber == 1 else "red"
        self.canvas.create_oval(cx - 25, cy - 25, cx + 25, cy + 25, fill = color, outline = color)

Animation()