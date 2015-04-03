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

        self.done = False

        self.redrawAll()
        root.mainloop()

    def distance(self, body1, body2):
        return ((body1.x - body2.x) ** 2 + (body1.y - body2.y)**2) ** .5

    def redrawAll(self):
        self.canvas.delete("all")
        for body in self.bodies:
            body.draw(self.canvas)
        for pivot in self.pivots:
            self.canvas.create_text(pivot.x, pivot.y, text = "P")

        self.canvas.update()

    def step(self, event):
        if(self.done): return

        # now move pivots to the centroid of it's cluster for the next step
        # if there is no change, than the clustering is done, otherwise, redraw everything
        oldPositions = [(pivot.x, pivot.y) for pivot in self.pivots]
        # dx, dy, assigned, pivot_id
        changes = [[0, 0, 0, pivot_id] for pivot_id in xrange(len(self.pivots))]
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

            self.bodies[body].color = self.pivots[maxPivot].color
            changes[maxPivot][0] += self.bodies[body].x
            changes[maxPivot][1] += self.bodies[body].y
            changes[maxPivot][2] += 1

        # for pivot in xrange(len(self.pivots)):
        #     print self.pivots[pivot], changes[pivot]

        # move each pivot
        for change in changes:
            if change[2] != 0:
                self.pivots[change[3]].x = change[0]/change[2]
                self.pivots[change[3]].y = change[1]/change[2]

        if oldPositions == [(pivot.x, pivot.y) for pivot in self.pivots]:
            print "Finished Clustering"
            self.done = True

        self.redrawAll()

try:
    Clustering(int(sys.argv[1]))
except:
    Clustering(10)
    