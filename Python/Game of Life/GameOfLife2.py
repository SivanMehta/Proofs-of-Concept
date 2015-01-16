from Tkinter import *

import time, random, copy
def makeRandomGrid(rows, cols):
    a = [[1] * rows for x in xrange(cols)]
    for r in xrange(rows):
        for c in xrange(cols):
            a[r][c] = random.choice([0,1])

    return a

class GameOfLife():
    def init(self):
        self.board = makeRandomGrid(self.rows, self.cols)
        self.directions = [ (-1, -1), (-1, 0), (-1, +1),
         ( 0, -1),          ( 0, +1),
         (+1, -1), (+1, 0), (+1, +1) ]
        self.mode = "playing"
        self.cellColor = "black"
        self.generation = 0

    def timerFired(self):
        # print self.mode
        if(self.mode == "playing"):
            self.canvas.delete(ALL)
            self.applyRules()
            self.redrawAll()
        elif(self.mode == "paused"):
            self.drawPauseScreen()
        # self.generation += 1
        # print self.paused
        # if(self.equilibrium):
        #     self.tests += [self.generation]
        # if(len(self.tests) > 150):
        #     print self.tests
        #     print "avg = ", sum(self.tests) /  150.0
        #     sys.exit()
        self.canvas.after(150, self.timerFired)

    def redrawAll(self):
        background = "white"
        self.canvas.create_rectangle(0,0, self.width, self.height, fill = background)
        for r in xrange(self.rows):
            for c in xrange(self.cols):        
                color = self.cellColor if self.board[r][c] == 1 else "white"
                self.canvas.create_rectangle(5 + r * 10, 5 + c * 10, 5 + (r + 1) * 10, 5 +(c + 1) * 10, outline = "white", fill = color)

    def drawPauseScreen(self):
        self.canvas.create_rectangle(self.width * .25, self.height * .33, self.width * .75, self.height * .67, fill = "white")
        self.canvas.create_text(self.height / 2, self.width / 2, text = "PAUSED", font = "Helvetica %d bold" % self.rows, fill = "red")

    def applyRules(self):
        # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        # Any live cell with two or three live neighbours lives on to the next generation.
        # Any live cell with more than three live neighbours dies, as if by overcrowding.
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        # ^^ taken from http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        a = copy.deepcopy(self.board)
        for r in xrange(self.rows):
            for c in xrange(self.cols):
                # print r , c
                neighbors = self.getLiveNeighbors(r,c)
                if(self.board[r][c] == 1): # if alive
                    if(neighbors < 2 or neighbors > 3):
                        a[r][c] = 0
                else:
                    if(neighbors == 3):
                        a[r][c] = 1
        self.board = a

        #generation handling
        # if(self.equilibrium == False and (self.board == self.penultimate)):
        #     # print "equilibrium after %d generations" % self.generation
        #     # sys.exit()
        #     self.equilibrium = True
        #     # self.generationCount += [self.generation]
        

    def getLiveNeighbors(self,r,c):
        total = 0
        for direction in self.directions:
            x = direction[0]
            y = direction[1]
            if (r + x >= 0 and r + x < self.rows and c + y >= 0 and c + y < self.cols and self.board[r + x][c + y] == 1):
                total += 1

        return total

    def keyPressed(self, event):
        # pause handling
        if(event.keysym == "p" and self.mode == "playing"): #toggle pause
            self.mode = "paused"
        elif(event.keysym == "p" and self.mode == "paused"):
            self.mode = "playing"

        elif(event.keysym == "c"): #clear the board
            self.board = [[0] * self.cols for x in xrange(self.rows)] # clear the board
            # print self.board
            self.mode = "playing"

        elif(event.keysym == "n"): #make a new board
            self.board = makeRandomGrid(self.rows, self.cols) # make a new board
            # print self.board
            self.cellColor = "black"
            self.mode = "playing"
            self.generation = 0
            self.equilibrium = False


        elif(event.keysym == "d" and self.mode == "playing"):
            # print "hola!"
            self.mode = "draw"
            self.cellColor = "red"
            self.redrawAll()
        elif(event.keysym == "d" and self.mode == "draw"):
            self.mode = "playing"
            self.cellColor = "black"

        elif(event.keysym == 't'):
            print self.tests

    def mousePressed(self, event):
        # print event.x, event.y
        if(self.mode == "draw" and 0 < event.x < self.width and 0 < event.y < self.height):
            row = event.x / 10
            col = event.y / 10
            self.board[row][col] = int(not self.board[row][col])
            self.redrawAll()

    def run(self, rows = 50):
        self.root = Tk()
        self.rows = rows
        self.cols = self.rows
        self.width = 10 * rows + 10
        self.height = 10 * rows + 10
        self.canvas = Canvas(self.root, height = self.width, width = self.height)
        self.canvas.pack()
        self.root.bind("<Key>", self.keyPressed)
        self.root.bind("<Button-1>", self. mousePressed)
        self.init()
        self.timerFired()
        self.root.mainloop()

GameOfLife().run(30)