import Tkinter, math, time

def getCoords(elapsed):
    x = int(300 + 200 * math.cos(elapsed))
    y = int(300 + 200 * math.sin(elapsed))
    return (x, y)

def avg(arr):
    return sum(arr)*1.0/len(arr)

class Animate():
    def __init__(self):
        root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(root, height = 600, width = 600)
        self.canvas.pack()

        self.radius = 75

        self.start_time = time.time()
        self.canvas.create_oval(getCoords(self.start_time)[0] - self.radius,
                                getCoords(self.start_time)[1] - self.radius,
                                getCoords(self.start_time)[0] + self.radius,
                                getCoords(self.start_time)[1] + self.radius,
                                fill = "#FF0000", outline = "#FF0000")

        self.canvas.create_text(300, 300, text = "", anchor = "center", font = "Courier 12")

        self.timer()

        root.mainloop()

    def timer(self):
        coords = self.canvas.coords(1)
        current_center_x = avg([coords[0], coords[2]])
        current_center_y = avg([coords[1], coords[3]])

        new_coords = getCoords(time.time())

        dx = new_coords[0] - current_center_x
        dy = new_coords[1] - current_center_y

        self.canvas.move(1, dx, dy)
        self.canvas.itemconfig(2, text = " Center: \n" + str(new_coords))
        self.canvas.update()
        self.canvas.after(1, self.timer)



Animate()