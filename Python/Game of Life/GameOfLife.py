from Tkinter import *

import time, random, copy
rows = cols = 60
# board = "hello!"
def makeRandomGrid():
    a = [[0] * rows for x in xrange(cols)]
    for r in xrange(rows):
        for c in xrange(cols):
            a[r][c] = random.choice([0,0,0,1])
    return a

board = makeRandomGrid()
print "here"
root = Tk()
width = 10 * cols + 10
height = 10 * rows + 10
canvas = Canvas(root, height = width, width = height)
canvas.pack()

def timerFired():
    canvas.delete(ALL)
    # board = makeRandomGrid()
    # print board
    redrawALl()
    applyRules()
    # redrawALl()
    # applyRules()
    # redrawALl()
    canvas.after(50, timerFired)

def redrawALl():
    canvas.create_rectangle(0,0,width, height, fill = "white")
    for r in xrange(rows):
        for c in xrange(cols):
            color = "black" if board[r][c] == 1 else "white"
            canvas.create_rectangle(5 + r * 10, 5 + c * 10, 5 + (r + 1) * 10, 5 +(c + 1) * 10, outline = "white", fill = color)
"""
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

def applyRules():
    # print "now here"
    # a = copy.deepcopy(board)
    for r in xrange(rows):
        for c in xrange(cols):
            neighbors = getLiveNeighbors(r,c)
            if(board[r][c] == 1): # if alive
                if(neighbors < 2 or neighbors > 3):
                    board[r][c] = 0
            else:
                if(neighbors == 3):
                    board[r][c] = 1
    # board = a

directions = [ (-1, -1), (-1, 0), (-1, +1),
     ( 0, -1),          ( 0, +1),
     (+1, -1), (+1, 0), (+1, +1) ]

def getLiveNeighbors(r,c):
    # return random.choice([0,1,2,3,4])
    total = 0
    for direction in directions:
        x = direction[0]
        y = direction[1]
    # for x in [-1, 0, 1]:
    #     for y in [-1, 0, 1]:
        if (r + x >= 0 and r + x < rows and c + y >= 0 and c + y < cols and board[r + x][c + y] == 1):
            total += 1

    # print r, c, total
    return total
        

timerFired()
root.mainloop()