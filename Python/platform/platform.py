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
        
        player = Rectangle(80, 80, 100, 100, "black")
        ground = Rectangle(-10, 600, 610, 601, "black") # the invisible ground at the bottom of the screen

        platform1 = Rectangle(0,  400,50,  410, generateRandomColor())
        platform2 = Rectangle(50, 400,100, 410, generateRandomColor())
        platform3 = Rectangle(100,400,150, 410, generateRandomColor())
        platform4 = Rectangle(150,400,200, 410, generateRandomColor())
        platform5 = Rectangle(200,400,250, 410, generateRandomColor())


        platform1a = Rectangle(350, 440,400, 450, generateRandomColor())
        platform2a = Rectangle(400, 440,450, 450, generateRandomColor())
        platform3a = Rectangle(450, 440,500, 450, generateRandomColor())
        platform4a = Rectangle(500, 440,550, 450, generateRandomColor())
        platform5a = Rectangle(550, 440,600, 450, generateRandomColor())
        
        self.player = player.draw(self.canvas)

        self.platforms = {
                            ground.draw(self.canvas)    : ground,

                            platform1.draw(self.canvas) : platform1,
                            platform2.draw(self.canvas) : platform2,
                            platform3.draw(self.canvas) : platform3,
                            platform4.draw(self.canvas) : platform4,
                            platform5.draw(self.canvas) : platform5,

                            platform1a.draw(self.canvas) : platform1a,
                            platform2a.draw(self.canvas) : platform2a,
                            platform3a.draw(self.canvas) : platform3a,
                            platform4a.draw(self.canvas) : platform4a,
                            platform5a.draw(self.canvas) : platform5a
                            }

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
        for platform_id in self.platforms.keys():
            platform = self.platforms[platform_id]
            if(self.player in self.canvas.find_overlapping(platform.x1, platform.y1, platform.x2, platform.y2)):
                return platform_id

    def sitting(self):
        self.canvas.move(self.player, 0, 1)
        sitting = self.hittingPlatform()
        self.canvas.move(self.player, 0, -1)

        return sitting

    def offScreen(self):
        return self.player not in self.canvas.find_overlapping(10,10,600,600)

    def animate(self):
        # pseudo friction for both the air and the ground
        if(abs(self.dx) > .0001):
            self.dx *= .95
        else:
            self.dx = 0

        self.canvas.move(self.player, self.dx, self.dy)
        # if you are going to the hit a box, go to the top of the box
        while(self.hittingPlatform()):
            self.canvas.move(self.player, 0, -1)
            self.dy = 0
        while(self.offScreen()):
            self.canvas.move(self.player, -(self.dx/abs(self.dx)), 0)
        self.dy += 1 # acceleration due to gravity

        if(self.sitting()):
            platform = self.sitting()
            self.canvas.itemconfig(self.player, fill = self.platforms[platform].color, outline = self.platforms[platform].color)
        else:
            self.canvas.itemconfig(self. player, fill = "black", outline = "white")

        self.canvas.update()

    def jump(self):
        self.dy = -15

    def move(self, direction):
        if direction == "R":
            self.dx += 5
        else:
            self.dx -= 5



Animation()