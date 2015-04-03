import random, math, sys, Tkinter, time, helper

class Body():
    def __init__(self, color):
        self.x = helper.uniform(0, 750)
        self.y = helper.uniform(0, 750)
        self.color = color

    def draw(self, canvas):
        canvas.create_oval(self.x - 4, self.y - 4, self.x + 4, self.y + 4, outline = self.color, fill = self.color)

    def __str__(self):
        return "(%d, %d) %s" % (self.x, self.y, self.color)

class Clustering():
    def __init__(self, clusters):
        root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(root, height = 750, width = 750)
        self.canvas.pack()

        self.bodies = [Body("grey") for i in xrange(10000)]
        self.pivots = [Body(helper.generateRandomColor()) for i in xrange(clusters)]
        self.done = False
        self.start = time.time()

        self.timer()
        self.redrawAll()
        root.mainloop()

    def distance(self, body1, body2):
        return ((body1.x - body2.x) ** 2 + (body1.y - body2.y)**2) ** .5

    def redrawAll(self):
        self.canvas.delete("all")
        for body in self.bodies:
            body.draw(self.canvas)
        for pivot in self.pivots:
            self.canvas.create_oval(pivot.x-7, pivot.y-7, pivot.x+7, pivot.y+7, fill = "white")
            self.canvas.create_text(pivot.x, pivot.y, text = "P")

        self.canvas.update()

    def timer(self):
        if self.step():
            self.canvas.after(1, self.timer)

    def step(self):
        if(self.done): return False

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
            print "Finished Clustering after %.2f seconds" % (time.time() - self.start)
            self.done = True

        self.redrawAll()

        return True

try:
    Clustering(int(sys.argv[1]))
except:
    Clustering(10)
    