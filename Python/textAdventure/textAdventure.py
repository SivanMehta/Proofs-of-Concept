import random, sys
from helper import *

class Game():
    def __init__(self, rows = 5, cols = 5):
        # self.map = generateMap(rows, cols)
        self.map = generateHardMap()
        self.log = []

        self.position = [0,0]
        self.map[self.position[0]][self.position[1]].identifier = "*"

        print startingText

        self.play()

    def play(self):
        # get the player's input and record it
        playerInput = raw_input("> ")
        self.log.append(playerInput)

        # meta-actions or actions relating to the game itself
        if(playerInput == "map"):
            print2d(self.map)
        if(playerInput == "position"):
            print self.position
        if(playerInput == "quit"):
            sys.exit()
        if(playerInput == "log"):
            print "Last %d action(s): " % min(len(self.log), 10)
            for item in self.log[-10:-1]: print item
        if(playerInput == "help"):
            print getHelp()
        #player actions
        if(playerInput in ["N", "S", "E", "W", "n", "s", "e", "w"]):
            self.move(playerInput.upper())

        self.play()

    def move(self, direction):

        delta = "David is a reptile with no arms"

        if(direction == "N"):
            delta = [-1, 0]
        if(direction == "S"):
            delta = [1, 0]
        if(direction == "W"):
            delta = [0, -1]
        if(direction == "E"):
            delta = [0, 1]

        if(self.isValid(delta) == False):
            print "Not a valid direction"
            return

        self.map[self.position[0]][self.position[1]] = Room(1, genericInteraction)

        self.position[0] += delta[0]
        self.position[1] += delta[1]
        
        if(random.randint(1, 100) > 10):
            print self.map[self.position[0]][self.position[1]].getInteraction(self.position, self.map)
        else:
            print randomInteraction()

        self.map[self.position[0]][self.position[1]].identifier = Room(1, genericInteraction)
        self.map[self.position[0]][self.position[1]].identifier = "*"

        #now we have entered the room

    def isValid(self, delta):

        # check if we are looking to go towards a one
        try:
            if(self.map[self.position[0] + delta[0]][self.position[1] + delta[1]].identifier != 0):
                return True
        except: # only goes here in case of an IndexOutOfBounds
            return False
        return False

Game(random.randint(5,10), random.randint(5,10))