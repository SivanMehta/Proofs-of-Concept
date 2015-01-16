import math
from Tkinter import *

root = Tk()
cx = 500
cy = 500
canvas = Canvas(root, width = cx, height = cy)
canvas.pack()

def almostEquals(x, y):
    return (abs(x - y) < .01)

def drawPoint(x, y, color):
    canvas.create_oval(x, y, x, y, fill = color, outline = color)

def drawCartesianFunction(f):
    for x in xrange(-500, 500): # 500 is the width of the canvas
        drawPoint(250 + x, 250 - f(x) / 100, "black")

def drawPolarPoint(r, t, color): # t = theta in radians
    #250, 250 is the center
    # 1 radius will be 20 pts
    r *= 50
    drawPoint(250 + r * math.cos( t), 250 - r * math.sin(t), color)

def drawPolarFunction(f):
    #we want to draw at least one 1 period
    theta = .01

    while(theta < 8 * math.pi):
        drawPolarPoint(f(theta), theta, "red")
        theta += .01

def g(x): # the Cartesian function g(x) = x ** 2
    return x ** 2

def r1(theta): # the polar function r = 2cos(3 * theta)
    return 2 * math.cos( 3 * theta )

def run():
    canvas.create_line(250, 0, 250, 500)
    canvas.create_line(0, 250, 500, 250)
    # canvas.create_text(10,500,text = "Polar and Cartesian graphs are not on the same scale", anchor = "sw")
    drawPolarFunction(r1)

run()

root.mainloop()