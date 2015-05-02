import random, helper
from Tkinter import *
root = Tk()
canvas = Canvas(root, height = 500, width = 500)
canvas.pack()

canvas.create_text(150, 150, text = "p")
canvas.create_text(350, 350, text = "p")

x_plots = []

def cluster(x, y, points):
    for i in xrange(points):
        plot_x = random.normalvariate(x, 10)
        plot_y = random.normalvariate(y, 10)
        color = helper.generateRandomColor()
        canvas.create_oval(plot_x - 5, plot_y - 5, plot_x + 5, plot_y + 5, fill = color, outline = color)


cluster(250, 250, 1000)
root.mainloop()