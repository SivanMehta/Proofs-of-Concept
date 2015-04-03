import random, math, Tkinter

# assumed to have radius 5
class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.randint(-5, 3)
        self.dy = random.randint(-3, 3)

    def draw(self, canvas):
        return canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill = "brown", outline = "brown")

    def collides(self, other):
        # distance between two centers is less than the sum of their radii
        # print (self.dx**2 + self.dy**2)**.5
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**.5 < 20

    def resolveCollision(self, other):
        if(other.y == self.y): return

        theta = math.pi - math.atan((other.x - self.x)/(other.y - self.y))
        speed = (self.dx**2 + self.dy**2)**.5
        self.dx = speed * math.cos(theta)
        self.dy = speed * math.sin(theta)


class Brownian():
    def __init__(self, particles = 2):
        root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(root, width = 600, height = 600)
        self.canvas.pack()

        self.particles = {}
        # for i in xrange(particles):
        #     obj = Particle(random.randint(10, 590), random.randint(15, 590))
        #     self.particles[obj.draw(self.canvas)] = obj

        obj1 = Particle(200, 295)
        obj1.dx, obj1.dy = 1,0
        obj2 = Particle(400, 305)
        obj2.dx, obj2.dy = -1,0

        self.particles = {
            obj1.draw(self.canvas) : obj1,
            obj2.draw(self.canvas) : obj2
        }

        self.timer()
        root.mainloop()

    def timer(self):
        self.animate()
        self.canvas.after(1, self.timer)

    def animate(self):
        # walls
        for key in self.particles.keys():
            particle = self.particles[key]

            if((particle.dx > 0 and particle.x > 590) or (particle.dx < 0 and particle.x < 10)):
                particle.dx *= -1

            if((particle.dy > 0 and particle.y > 590) or (particle.dy < 0 and particle.y < 15)):
                particle.dy *= -1

            self.canvas.move(key, particle.dx, particle.dy)
            particle.x += particle.dx
            particle.y += particle.dy

        # other particles
        for p1 in self.particles.keys():
            particle1 = self.particles[p1]
            for p2 in self.particles.keys():
                particle2 = self.particles[p2]
                if (p1 != p2):
                    if(particle1.collides(particle2)):
                        # print p1,
                        particle1.resolveCollision(particle2)
                        particle1.dy *= -1

        self.canvas.update()


Brownian(25)