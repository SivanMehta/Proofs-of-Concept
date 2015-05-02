import random
from Tkinter import *
root = Tk()
canvas = Canvas(root, height = 500, width = 500)
canvas.pack()


x_plots = []

def cluster(x, y, points):
    for i in xrange(points):
        plot_x = random.normalvariate(x, 10)
        plot_y = random.normalvariate(y, 10)
        color = helper.generateRandomColor()
        canvas.create_oval(plot_x - 5, plot_y - 5, plot_x + 5, plot_y + 5, fill = color, outline = color)

cluster(150, 150, 500)
canvas.create_oval(140, 140, 160, 160, fill = "white")
canvas.create_text(150, 150, text = "c")

cluster(350, 350, 500)
canvas.create_oval(340, 340, 360, 360, fill = "white")
canvas.create_text(350, 350, text = "c")

root.mainloop()