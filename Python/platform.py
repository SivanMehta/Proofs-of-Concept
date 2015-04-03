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

class Square():
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.radius = diameter / 2
        self.color = color
        self.dx = 0
        self.dy = 0

    def draw(self, canvas):
        return canvas.create_rectangle(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius,
            fill = self.color, outline = self.color)

class Animation():
    def __init__(self):
        root = Tk()
        root.bind("<Key>", self.eventOccurs)
        self.canvas = Canvas(root, width = 600, height = 600)
        self.canvas.pack()
        
        box = Square(400, 390, 20, "black")
        ground = Square(300, 700, 600, "red")
        
        self.player = box.draw(self.canvas)

        self.ground = ground.draw(self.canvas)

        self.dy = 0
        self.dx = 0
        self.text = self.canvas.create_text(100, 50, text = "")

        self.canvas.update()
        self.timer()
        mainloop()

    def eventOccurs(self, event):
        if (event.keysym in ["space", "Up"]):
            self.jump()
        if (event.keysym in ["Right", "Left"]):
            self.move(event.keysym[0])

    def timer(self):
        self.animate()
        self.canvas.after(10, self.timer)

    def animate(self):
        # self.canvas.itemconfig(self.text, text = "dx:%f dy:%f" % (self.dx, self.dy))

        # pseudo friction
        if(abs(self.dx) > .0001):
            self.dx *= .9
        else:
            self.dx = 0

        
        self.canvas.move(self.player, self.dx, self.dy)

        # if you are going to the hit the box, go to the top of the box
        while(self.player in self.canvas.find_overlapping(0, 400, 600, 600)):
            self.canvas.move(self.player, 0, -1)
            self.dy = 0
        
        self.dy += 1

        self.canvas.update()

    def jump(self):
        self.dy = -20

    def move(self, direction):
        if direction == "R":
            self.dx += 5
        else:
            self.dx -= 5



Animation()