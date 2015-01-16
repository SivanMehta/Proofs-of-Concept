from Tkinter import *

class Box():
    def __init__(self, x1 = 0, y1 = 0, x2 = 10, y2 = 10):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.height = self.y2 - self.y1
        self.width = self.x2 - self.x1

        self.vx = 0
        self.vy = 0

    def move(self, keysym):
        if(keysym == "Right"):
            self.vx += 20
        if(keysym == "Left"):
            self.vx -= 20
        if(keysym == "Up"):
            self.vy -= 100

    def animate(self):
        self.x1 += self.vx
        self.x2 += self.vx

        self.y1 += self.vy
        self.y2 += self.vy

        # pseudo-friction
        self.vx *= .9

        if(abs(self.vx) <= .001): self.vx = 0

        #pseudo-gravity
        self.vy += 10

        if(self.y1 < 0):
            self.y1 = 0
            self.y2 = self.height
            self.vy = 0
        if(self.x1 < 0):
            self.x1 = 0
            self.x2 = self.width
            self.vx = 0
        if(self.x2 > 500):
            self.x2 = 500
            self.x1 = 500 - self.width
            self.vx = 0
        if(self.y2 > 500):
            self.y2 = 500
            self.y1 = 500 - self.height
            self.vy = 0
        

    def collides(self, B):
        A = self
        return (A.x1 <= B.x2) and (A.x2 >= B.x1) and (A.y1 <= B.y2) and (A.y2 >= B.y1)   

class PlatformAnimation():
    def __init__(self):
        self.environment = []

        self.environment.append(Box(100, 400, 200, 450))
        self.environment.append(Box(200, 350, 300, 400))
        self.environment.append(Box(300, 300, 400, 350))

        self.player = Box(0, 0, 50, 50)

        self.root = Tk()
        self.canvas = Canvas(self.root, height = 500, width = 500)
        self.canvas.pack()

        self.root.bind("<Key>", self.keyPressed)

        self.timer()
        self.root.mainloop()

    def draw(self):
        self.canvas.delete(ALL)
        
        collides = False
        for platform in self.environment:
            if platform.collides(self.player):
                color = "red"
                collides = True
            else:
                color = "blue"
            self.canvas.create_rectangle(platform.x1, platform.y1, platform.x2, platform.y2, fill = color, outline = color)

        if(collides):
            color = "red"
        else:
            color = "blue"
        self.canvas.create_rectangle(self.player.x1, self.player.y1, self.player.x2, self.player.y2, fill = color, outline = color)

    def keyPressed(self, event):
        self.player.move(event.keysym)
        self.draw()

    def timer(self):
        self.player.animate()

        for platform in self.environment:
            if (platform.collides(self.player) and self.player.x2 >= platform.x1 and self.player.y2 >= platform.y1): # if square B is on top of square A, stop vertical motion
                self.player.vy = 0

        self.draw()
        self.canvas.after(50, self.timer)

PlatformAnimation()