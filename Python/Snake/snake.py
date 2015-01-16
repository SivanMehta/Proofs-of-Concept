from Tkinter import *
import time, copy, sys, random

class PhysicalObject():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, canvas):
        canvas.create_rectangle(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color, outline = self.color)

    def collides(self, other):
        return (self.x == other.x and self.y == other.y)

class Snake():
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, height = 500, width = 500)
        self.canvas.pack()
        self.root.bind("<Key>", self.keyInput)

        self.notInit()
        self.timer()

        self.root.mainloop()

    def notInit(self):
        self.snake = [PhysicalObject(300, 300, 10, "red")]
        self.snake[0].color = "green"
        self.coin = PhysicalObject(200, 200, 10, "blue")
        self.direction = [0, -1]

    def keyInput(self, event):
        if(event.keysym == "Up"):
            self.direction = [0, -1]
        if(event.keysym == "Down"):
            self.direction = [0, 1]
        if(event.keysym == "Left"):
            self.direction = [-1, 0]
        if(event.keysym == "Right"):
            self.direction = [1, 0]

    def timer(self):
        self.animate()
        self.redrawAll()

        self.canvas.after(100, self.timer)

    def animate(self):
        oldSnake = copy.deepcopy(self.snake) # http://en.wikipedia.org/wiki/Metal_Gear_Solid

        for i in range(1, len(self.snake)):
            self.snake[i].x = oldSnake[i - 1].x
            self.snake[i].y = oldSnake[i - 1].y

        head = self.snake[0]
        head.x += 20 * self.direction[0]
        head.y += 20 * self.direction[1]

        tail = [self.snake[-1].x, self.snake[-1].y]
        hits = False

        for segment in self.snake:
            if head.collides(segment) and segment != head or (head.x <= 0 or head.y <= 0 or head.x >= 500 or head.y >= 500):
                self.end()
                sys.exit()

        if head.collides(self.coin):
            self.eat()

        # oldSnake? oldSnake?!?! OLDSNAKE!!!!!!!!!!!!

    def eat(self):
        self.coin.color = "#0666D0"
        self.snake += [self.coin]

        self.coin = PhysicalObject(random.randint(4, 22) * 20, random.randint(4, 22) * 20, 10, "blue")

        while any([self.snake[i].collides(self.coin) for i in xrange(len(self.snake))]): # any(x) returns x[0] or x[1] or x[2]....
            self.coin.x, self.coin.y = random.randint(4, 22) * 20, random.randint(4, 22) * 20 # randomly reassign coin      

    def end(self):
        highScore = 0
        with open("highscore.txt", mode = "r") as f:
            contents = f.read()
            highScore = max(int(contents[int(contents.index(":")) + 2:]), len(self.snake))
        with open("highscore.txt", mode = "w") as f:
                f.write("Your current high score is: %d" % highScore)
        with open("highscore.txt", mode = "r") as f:
            print f.read()        

    def redrawAll(self):
        self.canvas.delete(ALL)
        for segment in self.snake:
            segment.draw(self.canvas)

        self.coin.draw(self.canvas)
        self.canvas.create_text(450, 50, text = str(len(self.snake)))

Snake()