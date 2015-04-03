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

class Rectangle():
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.dx = 0
        self.dy = 0

    def draw(self, canvas):
        return canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.color, outline = self.color)

class Animation():
    def __init__(self):
        root = Tk()
        root.bind("<Key>", self.eventOccurs)
        self.canvas = Canvas(root, width = 600, height = 600)
        self.canvas.pack()
        
        player = Rectangle(500, 200, 520, 220, "black")

        ground = Rectangle(0, 400, 600, 600, "blue")

        platform1 = Rectangle(400, 300, 600, 310, "brown")
        platform2 = Rectangle(200,200,300, 210, "brown")
        
        self.player = player.draw(self.canvas)

        self.platforms = [
        (ground.draw(self.canvas), ground),
        (platform1.draw(self.canvas), platform1),
        (platform2.draw(self.canvas), platform2)
        ]

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

    def hittingPlatform(self):
        for platform_id, platform in self.platforms:
            if(self.player in self.canvas.find_overlapping(platform.x1, platform.y1, platform.x2, platform.y2)):
                return True

    def animate(self):
        # pseudo friction
        if(abs(self.dx) > .0001):
            self.dx *= .9
        else:
            self.dx = 0

        self.canvas.move(self.player, self.dx, self.dy)
        # if you are going to the hit the box, go to the top of the box
        while(self.hittingPlatform()):
            self.canvas.move(self.player, 0, -1)
            self.dy = 0  
        self.dy += 1

        self.canvas.update()

    def jump(self):
        self.dy = -15

    def move(self, direction):
        if direction == "R":
            self.dx += 5
        else:
            self.dx -= 5



Animation()