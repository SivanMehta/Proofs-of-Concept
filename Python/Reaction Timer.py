from Tkinter import *
import time, random

class Reactions():
    def __init__(self):
        self.trialStarted = False
        self.started = False
        self.trials = 0
        self.totalTime = 0
        self.average = 0
        self.cheated = False
        self.trialStartTime = None
        self.trialEndTime = None
        self.last = None

    def doTrial(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill = "#D30B13") # red
        self.canvas.create_text(300, 200, font = "Nanum\ Brush\ Script 36 bold", text = "Wait for Green", fill = "white")

        if(self.cheated):
            self.canvas.create_rectangle(200, 300, 400, 380, fill = "white")
            self.canvas.create_text(300, 340, text = "Don't Click Early", font = "Nanum\ Brush\ Script 30 bold")
            self.cheated = False;
        elif(self.started):
            self.canvas.create_text(500, 50, text = "Trials: " + str(self.trials), font = "Nanum\ Brush\ Script 20 bold", fill = "white")
            self.canvas.create_text(500, 70, text = "Average: " + str(self.average), font = "Nanum\ Brush\ Script 20 bold", fill = "white")
            self.canvas.create_text(500, 90, text = "Last: " + str(self.last), font = "Nanum\ Brush\ Script 20 bold", fill = "white")

        self.canvas.after(random.choice(range(2000, 5000)), self.drawClickScreen) # waits anywhere from 3 to 5 seconds, and then draws click screen

    def drawClickScreen(self):
        self.trialStarted = True
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill = "#33BB00") # green

        self.trialStartTime = time.time()
        self.canvas.create_text(300, 200, font = "Nanum\ Brush\ Script 50 bold", text = "CLICK!", fill = "white")

    def mousePressed(self, event):
        if (self.trialStarted):

            self.trialEndTime = time.time()
            trialTime = self.trialEndTime - self.trialStartTime
            self.last = int ( trialTime * 1000 )
            self.totalTime += trialTime * 1000

            self.trials += 1
            self.average = int( self.totalTime / self.trials )
        else:
            self.cheated = True;  
            self.drawClickScreen()  

        self.trialStarted = False
        self.started = True
        self.doTrial()


    def run(self):
        root = Tk()
        self.height = 400
        self.width = 600
        self.canvas = Canvas(root, width = self.width, height = self.height)
        self.canvas.pack()
        root.bind("<Button-1>", self.mousePressed)
        self.doTrial()
        root.mainloop()

Reactions().run()