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
        self.radius = radius
        self.x = x
        self.y = y
        self.color = generateRandomColor()

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color, outline = self.color)
        # canvas.create_rectangle(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color, outline = self.color)

    def inBounds(self, x, y):
        return (self.x - x) ** 2 + (self.y - y) ** 2 <= self.radius ** 2
        # return (self.x - self.radius <= x and x <= self.x + self.radius) and (self.y - self.radius <= y and y <= self.y + self.radius)

    def __str__(self):
        return "(%d, %d) with radius %d" % (self.x, self.y, self.radius)


class dotAnimation():
    def __init__(self):
        self.root = Tk()
        self.root.bind("<Key>", self.keyPressed)
        self.root.bind("<Button-1>", self.mousePressed)
        # self.root.bind("<Motion>", self.mousePressed)
        self.size = 512
        self.canvas = Canvas(self.root, width = self.size, height = self.size)
        self.canvas.pack()
        self.level = 1
        self.circles = [circle(256, 256, 256)] # start with one circle initially
        #this holds the circles with centers as keys and the circle itself as the value
        

    def run(self):
        self.redrawAll()
        self.root.mainloop()

    def keyPressed(self, event):
        if(event.keysym == "r"):
            self.circles = [circle(256, 256, 256)]
        self.redrawAll()

    def mousePressed(self, event):

        for x in xrange(len(self.circles)):
            if(self.circles[x].inBounds(event.x, event.y)):
                
                splitter = self.circles[x]

                self.circles.remove(splitter)

                one = circle(splitter.x - splitter.radius / 2, splitter.y - splitter.radius / 2, splitter.radius / 2)
                two = circle(splitter.x + splitter.radius / 2, splitter.y - splitter.radius / 2, splitter.radius / 2)
                three = circle(splitter.x - splitter.radius / 2, splitter.y + splitter.radius / 2, splitter.radius / 2)
                four = circle(splitter.x + splitter.radius / 2, splitter.y + splitter.radius / 2, splitter.radius / 2)
                self.circles.append(one)
                self.circles.append(two)
                self.circles.append(three)
                self.circles.append(four)

                break

        self.redrawAll()

    def split(self, direction):
        #handle bounds cases
        if(self.level == 7 and direction == 1):
            return
        if(self.level == 1 and direction == -1):
            return

        if(direction == 1):
            self.level += 1
        else:
            self.level -= 1

        self.redrawAll()

    def redrawAll(self):
        self.canvas.delete(ALL)
        # radius = self.size / (2 ** self.level)
        # for x in xrange(2 ** (self.level - 1)):
        #     for y in xrange(2 ** (self.level - 1)):
        #         circle(radius + 2 * x * radius, radius + 2 * y * radius, radius).draw(self.canvas)
        for circle in self.circles:
            circle.draw(self.canvas)

#############
## Testing ##
#############

dotAnimation().run()