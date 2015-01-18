from Tkinter import *
import time

###############
## Utilities ##
###############

konami = ['Up', 'Up', 'Down', 'Down', 'Left', 'Right', 'Left', 'Right', 'b', 'a']

def commas(a): #returns a number written with the commas (12354 --> 12,345)
    representation = ""
    backwards = str(a)[::-1] # a string of the number backwards
    for i in xrange(len(backwards)): # iterate backwards
        representation = backwards[i] + representation
        if(i % 3 == 2):
            representation = ',' + representation

    if(len(backwards) % 3 == 0): # so we don't get something like ,123,456
        return representation[1:]
    return representation

class Button():
    def __init__(self, name, price, output):
        self.name = name
        self.truePrice = price
        self.price = price
        self.output = output
        self.hidden = True
        self.quantity = 0

    def __str__(self): # for debugging purposes
        string = ""
        string += "Name: " + self.name + "\n"
        string += "Price: " + str(self.price) + "\n"
        string += "Output: " + str(self.output) + "\n"
        string += "Quantity: " + str(self.quantity) + "\n"
        return string

class Clicker():
    def __init__(self):
        self.gameStarted = False
    
    def init(self):
        # self.startTime = 0
        self.buttons = []
        self.cookiesPerSecond = 0
        self.cookies = 0
        # col 1
        self.buttons += [ Button("EZ Bake Oven", 15, 1) ]
        self.buttons += [ Button("Grandma", 100, 15) ]
        self.buttons += [ Button("Farm", 500, 100) ]
        self.buttons += [ Button("Factory", 3000, 500)  ]
        # col 2
        self.buttons += [ Button("Batter Mine", 10000, 3000) ]
        self.buttons += [ Button("Cookie Meteor",40000, 10000) ]
        self.buttons += [ Button("Portal to Cookieverse", 200000, 40000)]
        self.buttons += [ Button("Anticookie Condenser", 1234567, 200000) ]
        self.keysPressed = []

    def redrawAll(self):
        #buttons

        self.canvas.create_oval(300 - 50, 75 - 50, 300 + 50, 75 + 50, fill = "#43382B")
        self.canvas.create_text(300, 75, text = "FREE COOKIES", fill = "white")

        for x in xrange(4):
            #left column
            self.drawButton(5,5 + 150 * x, 205, 155 + 150 * x)
            curButton = self.buttons[x]
            self.canvas.create_text(105, 80 + 150 * x, text = curButton.name, fill = "white")
            self.canvas.create_text(105, 100 + 150 * x, text = commas(curButton.price), fill = "white")
            self.canvas.create_text(105, 120 + 150 * x, text = commas(curButton.quantity), fill = "white")
            if(self.cookies < curButton.price):
                self.canvas.create_line(5, 5 + 150 * x, 205, 155 + 150 * x, fill = "red", width = 10)
                self.canvas.create_line(5, 155 + 150 * x, 205, 5 + 150 * x, fill = "red", width = 10)

            #right column
            self.drawButton(400,5 + 150 * x, 600, 155 + 150 * x)
            curButton = self.buttons[x + 4]
            self.canvas.create_text(500, 80 + 150 * x, text = curButton.name, fill = "white")
            self.canvas.create_text(500, 100 + 150 * x, text = commas(curButton.price), fill = "white")
            self.canvas.create_text(500, 120 + 150 * x, text = commas(curButton.quantity), fill = "white")
            if(self.cookies < curButton.price):
                self.canvas.create_line(400,5 + 150 * x, 600, 155 + 150 * x, fill = "red", width = 10)
                self.canvas.create_line(400,155 + 150 * x, 600, 5 + 150 * x, fill = "red", width = 10)

        if(self.gameStarted == False):
            self.drawIntroScreen()
        else:
            self.canvas.create_text(300, 270, text = "Cookies:\n" + commas(self.cookies), justify = "center" )
            self.canvas.create_text(300, 300, text = "Cookies per Second:\n" + commas(self.cookiesPerSecond), justify = "center" )
            self.canvas.create_text(300, 330, text = "Time Elapsed: " + str(int(time.time() - self.startTime)), justify = "center")

    def drawButton(self, x0, y0, x1, y1): #draws a square with an outline
        #frame
        self.canvas.create_rectangle(x0,y0,x1,y1, fill = "#A26F37")
        #background
        self.canvas.create_rectangle(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill = "#43382B")

    def drawIntroScreen(self):
        self.canvas.create_rectangle(100, 100, 500, 500, fill = "white")
        self.canvas.create_text(300, 200, text = "COOKIE CLICKER", font =  "Marker\ Felt 35 bold")
        self.canvas.create_text(300, 400, text = "Click Anywhere to Start", font =  "Marker\ Felt 35 bold")

    def timerFired(self): # handles the visual updates
        self.canvas.delete(ALL)
        self.redrawAll()
        self.canvas.after(5, self.timerFired) # every 5 milliseconds, redraw the canvas because data might have changed

    def cookieTimer(self): # handles the cookies
        self.cookies += self.cookiesPerSecond
        self.canvas.after(1000, self.cookieTimer) #every 1 second, call timer again

    def mousePressed(self, event):
        # print event.x, event.y
        if(self.gameStarted):
            row = event.y / 150
            col = event.x / 200
            if(row > 3 or row < 0 or col < 0 or col > 2): return # if you are out of bounds, do nothing

            if(col == 1): #if you clicked in the middle
                col = None

            elif(col == 2): #if you clicked on the right side
                col = 1
            if(col == None):
                if((event.x - 300) ** 2 + (event.y - 75) ** 2 <= 50 ** 2): #if you clicked the "Free Cookies button"
                    self.cookies += 1
                return

            # otherwise you clicked one of the buttons
            curBut = self.buttons[row + col * 4]
            if(self.cookies >= curBut.price):
                self.cookiesPerSecond += curBut.output
                curBut.quantity += 1
                self.cookies -= curBut.price
                curBut.price = int(curBut.price * 1.11) # the buttons get more and more expensive as time goes on
        else:
            self.gameStarted = True
            self.startTime = time.time()

    def keyPressed(self, event):
        # print event.keysym
        self.keysPressed += [event.keysym]
        if(event.keysym == 'Escape'): # reset the game
            self.cookies = 0
            self.cookiesPerSecond = 0
            self.gameStarted = False
            for button in self.buttons:
                # print button
                button.price = button.truePrice
                button.quantity = 0
        elif(self.keysPressed[-10:] == konami and self.gameStarted): # cheat
            self.cookies = 2 ** 40
        self.keysPressed = self.keysPressed[-10:] # only need to save the last 10 keys

    def run(self):
        root = Tk()
        self.height = 600
        self.width = 600
        self.canvas = Canvas(root, width = self.width, height = self.height)
        self.canvas.pack()
        root.bind("<Button-1>", self.mousePressed)
        root.bind("<Key>", self.keyPressed)
        root.title("Cookie Clicker")
        self.init()
        self.timerFired()
        self.cookieTimer()
        root.mainloop()

Clicker().run()