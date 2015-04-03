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
        self.x = random.randint(0, 750)
        self.y = random.randint(0, 750)
        self.color = color

    def draw(self, canvas):
        canvas.create_oval(self.x - 4, self.y - 4, self.x + 4, self.y + 4, outline = self.color, fill = self.color)

    def __str__(self):
        return "(%d, %d) %s" % (self.x, self.y, self.color)

class Clustering():
    def __init__(self, clusters):
        root = Tkinter.Tk()
        root.bind("<Key>", self.step)
        root.bind("<Button-1>, self.step")
        self.canvas = Tkinter.Canvas(root, height = 750, width = 750)
        self.canvas.pack()

        self.bodies = [Body("grey") for i in xrange(10000)]

        self.pivots = [Body(generateRandomColor()) for i in xrange(clusters)]

        self.redrawAll()
        root.mainloop()

    def distance(self, body1, body2):
        return ((body1.x - body2.x) ** 2 + (body1.y - body2.y)**2) ** .5

    def redrawAll(self):
        self.canvas.delete()
        for body in self.bodies:
            body.draw(self.canvas)
        for pivot in self.pivots:
            self.canvas.create_text(pivot.x, pivot.y, text = "P")

        self.canvas.update()

    def step(self, event):
        # do nothing if bodies have already been clustered
        if (self.bodies[0].color != "grey"):
            print "Bodies already clustered"
            return

        print "clustering bodies, will assign by one of %d colors" % len(self.pivots)
        # for each body, assign it to a pivot
        assignments = []
        for body in xrange(len(self.bodies)):
            maxPivot = None
            minDistance = 750 * (2**.5) # max possible distance on the canvas
            for pivot in xrange(len(self.pivots)):
                distance = self.distance(self.pivots[pivot], self.bodies[body])
                if(distance < minDistance):
                    maxPivot = pivot
                    minDistance = distance

            assignments.append((body, maxPivot))

        for pair in assignments:
            body, pivot = pair
            self.bodies[body].color = self.pivots[pivot].color

        self.redrawAll()

if(len(sys.argv) == 2 and int(sys.argv[1]) > 1):
    Clustering(int(sys.argv[1]))
else:
    Clustering(10)
    