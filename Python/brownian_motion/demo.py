import random, Tkinter

# assumed to have radius 5
class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.randint(-5, 3)
        self.dy = random.randint(-3, 3)

    def draw(self, canvas):
        return canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill = "brown", outline = "brown")

class Brownian():
    def __init__(self, particles = 2):
        root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(root, width = 600, height = 600)
        self.canvas.pack()

        self.particles = {}

        for i in xrange(particles):
            obj = Particle(random.randint(10, 590), random.randint(15, 590))
            self.particles[obj.draw(self.canvas)] = obj

        self.timer()
        root.mainloop()

    def timer(self):
        self.animate()
        self.canvas.after(1, self.timer)

    def animate(self):
        for key in self.particles.keys():
            particle = self.particles[key]

            if((particle.dx > 0 and particle.x > 590) or (particle.dx < 0 and particle.x < 10)):
                particle.dx *= -1

            if((particle.dy > 0 and particle.y > 590) or (particle.dy < 0 and particle.y < 15)):
                particle.dy *= -1

            self.canvas.move(key, particle.dx, particle.dy)
            particle.x += particle.dx
            particle.y += particle.dy

        self.canvas.update()


Brownian(500)