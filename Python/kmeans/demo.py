import random, math, sys, Tkinter

def generateRandomColor():
    color = "#"
    for x in xrange(3):
        adding = hex( int(random.random() * 255) )[2:] #random number from 0 to 255 convert to hex
        if(len(adding) == 1):
            adding += "0"
        color += adding
    return color

class Body():
    def __init__(self, color):
        self.x = random.randint(10, 490)
        self.y = random.randint(10, 490)
        self.color = color

    def draw(self, canvas):
        canvas.create_oval(self.x - 4, self.y - 4, self.x + 4, self.y + 4, outline = self.color, fill = self.color)

    def __str__(self):
        return "(%d, %d) %s" % (self.x, self.y, self.color)

class Clustering():
    def __init__(self, clusters):
        root = Tkinter.Tk()
        root.bind("<Key>", self.step)
        self.canvas = Tkinter.Canvas(root, height = 500, width = 500)
        self.canvas.pack()

        self.bodies = [Body("grey") for i in xrange(100)]

        self.pivots = [(Body("red"), generateRandomColor()) for i in xrange(clusters)]

        self.draw()
        root.mainloop()

    def distance(self, body1, body2):
        return ((body1.x - body2.x) ** 2 + (body1.y - body2.y)**2) ** .5

    def draw(self):
        self.canvas.delete(ALL)
        for body in self.bodies: body.draw(self.canvas)
        for pivot in self.pivots:
            self.canvas.create_text(pivot[0].x, pivot[0].y, text = "P")

    def step(self, event):
        # do nothing if bodies have already been clustered
        if (self.bodies[0].color != "grey"):
            print "Bodies already clustered"
            return

        print "clustering bodies, will assign by color"
        # for each body, assign it to a pivot
        assignments = []
        for body in xrange(len(self.bodies)):
            maxPivot = None
            minDistance = 500 * (2**.5) # max possible distance on the canvas
            for pivot in xrange(len(self.pivots)):
                distance = self.distance(self.pivots[pivot][0], self.bodies[body])
                if(distance < minDistance):
                    maxPivot = pivot
                    minDistance = distance

            assignments.append((body, maxPivot))

            sys.stdout.flush()
            sys.stdout.write("\rassigned body %d/100... " % (body + 1))

        print "\033[0;32m DONE\033[0m"

        for pair in assignments:
            body, pivot = pair
            self.bodies[body].color = self.pivots[pivot][1]

        self.draw()

Clustering(10)