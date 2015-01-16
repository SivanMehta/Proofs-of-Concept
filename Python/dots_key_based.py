from Tkinter import *
import random

def generateRandomColor():
    color = "#"
    for x in xrange(3):
        adding = hex( int(random.random() * 255) )[2:] #random number from 0 to 255 convert to hex
        if(len(adding) == 1):
            adding += "0"
        color += adding
    return color

class circle():
    def __init__(self, x, y, radius):
        # max level is 8 as 2 ** 8 is 256 or the half height/width of the canvas (radius of the largest circle)
        self.radius = radius
        self.x = x
        self.y = y
        self.color = generateRandomColor()

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color, outline = self.color)


class dotAnimation():
    def __init__(self):
        self.root = Tk()
        self.root.bind("<Key>", self.keyPressed)
        self.size = 512
        self.canvas = Canvas(self.root, width = self.size, height = self.size)
        self.canvas.pack()
        self.level = 1
        self.starter = circle(256, 256, 256)
        #this holds the circles with centers as keys and the circle itself as the value
        

    def run(self):
        self.redrawAll()
        self.root.mainloop()

    def keyPressed(self, event):
        if(event.keysym == "Up"):
            self.split(1)
        elif(event.keysym == "Down"):
            self.split(-1)

    def split(self, direction):
        #handle bounds cases
        # if(self.level == 9 and direction == 1):
        #     return
        if(self.level == 1 and direction == -1):
            return

        if(direction == 1):
            self.level += 1
        else:
            self.level -= 1

        self.redrawAll()

    def redrawAll(self):
        self.canvas.delete(ALL)
        radius = self.size / (2 ** self.level)
        for x in xrange(2 ** (self.level - 1)):
            for y in xrange(2 ** (self.level - 1)):
                circle(radius + 2 * x * radius, radius + 2 * y * radius, radius).draw(self.canvas)

#############
## Testing ##
#############

dotAnimation().run()