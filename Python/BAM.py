# hello

import random
from Tkinter import *

root = Tk()
canvas = Canvas(root, width = 400, height = 400)
canvas.pack()
words = "How YOU doin"

if(len(words) <= 6):
    fontSize = 100
else:
    fontSize = 600 / len(words)

def average(numbers):
    return sum(numbers) * 1.0 / len(numbers)

def generateRandomColor():
    color = "#"
    for x in xrange(3):
        adding = hex( int(random.random() * 255) )[2:] #random number from 0 to 255 convert to hex
        if(len(adding) == 1):
            adding += "0"
        color += adding
    return color

def blackOrWhite(color):
    colors = color[1:]
    red = int(colors[0:2], 16)
    green = int(colors[2:4], 16)
    blue = int(colors[4:6], 16)

    if(average([red, green, blue]) < 127.5):
        return "white"
    else:
        return "black"

def do():
    canvas.delete(ALL)

    color = generateRandomColor()
    textColor = blackOrWhite(color)

    canvas.create_rectangle(0, 0, 400, 400, fill = color, outline = color)
    canvas.create_text(200, 200, text = words, font = "Futura %d" % fontSize, fill = textColor)
    
    canvas.after(1, do)


do()

root.mainloop()
