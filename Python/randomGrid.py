import random

grid = [ [0] * 5 for i in xrange(5) ]
indeces = range(1,26)

for row in xrange(len(grid)):
    for col in xrange(len(grid[row])):
        number = random.choice(indeces)
        grid[row][col] = number
        if len(indeces) > 1:
            indeces.remove(number)

from Tkinter import *
root = Tk()
canvas = Canvas(root, height = 500, width = 500)
canvas.pack()

for row in xrange(5):
    for col in xrange(5):
        val = grid[row][col]
        radius = val * 1.15

        canvas.create_oval(50 + col * 100 - radius, 50 + row * 100 - radius, 50 + col * 100 + radius, 50 + row * 100 + radius, fill = "#0666D0", outline = "#0666D0")
        canvas.create_text(50 + col * 100, 50 + row * 100, text = str(val), fill = "white" if val > 3 else "black")

root.mainloop()