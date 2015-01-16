import random, sys, copy, webbrowser

def getHelp():
    return """
    map --> shows the map and indicates with a "*" where you are
    N/E/S/W --> moves player in specified direction
    log --> shows recent moves
    quit --> quits the game
    *save --> saves the game
    *load --> loads the game
    """

def print2d(grid):
    for row in grid:
        for item in row: print item,
        print

def generateMap(rows, cols):
    # fill up board with zeroes
    board = [[0]*cols for row in xrange(rows)]

    # make a path with ones
    for col in xrange(cols / 2):
        board[0][col] = 1

    for row in xrange(rows):
        board[row][cols / 2] = 1

    for col in xrange(cols / 2, cols):
        board[rows - 1][col] = 1

    return board

def randomInteraction():
    roll = random.randint(1,4)

    if(roll == 1):
        return """
        Upon discovering that you haven't eaten in thirty hours since recovering from the  Gallo challenge, you realize that your still weary innards are in desparate need of nourishment. 

        "WHY MUST YOU TORTURE ME?!" you cry, trembling in terror as you hear quesadillas get burned by some illiterate chick in the distance"""
    if(roll == 2):
        a = raw_input("""
        As you traipse aimlessly through the grease ridden hallways of the Gallows de Gallo, your nostrils take in a remarkably familiar scent, one that fills your heart with dread and your loins with fire. Your delicate butthole quivers as the realization of what is placed on a pedestal in front of you sinks in: a Gallo double burrito. Your stomach yearns for sustinance, but can your poop chute handle it?

        A. Eat the burrito
        B. Leave the burrito
        C. Shove the burrito up your butthole
        --> """)
        if(a.upper() == "A"): return "Do it for mother, Clarence. Be stronk"
        elif(a.upper() == "B"): return "I am truly sorry that you descended this far into sanity, may your anus have mercy on your soul"
        elif(a.upper() == "C"): return "Turn off the computer, you sick fuck"
        else: return "Good Answer"
    if(roll == 3):
        a = raw_input("""
        You meet a strange traveler who seems wise beyond his years. You tell him about the hardships your digestive system has endured, and the truly vicious trials of agony they have been subjected to, with every syllable driving your psyche further into madness. To seek his obviously wise council, you ask him a question that seemingly only he can answer.
        What is your question, lost one?
        --> """)
        return """
        The wise man turns to you and says, with the utmost of concern

        'What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.'
        \nHe then kicks you in balls and takes all your money.
        """
    if(roll == 4):
        print """
        The game.
        You are now manually breathing.
        Everytime you swallow, you hear static.
        There is no comfortable place in your mouth for your tongue.
        You CAN see your nose between your eyes.
        Your clothes are touching your skin.
        """

        webbrowser.open("http://www.youtube.com/watch?v=oHg5SJYRHA0")

        return "Sorry, I'm not sorry"

def genericInteraction(position, map):
    return "You have entered a %s room!" % map[position[0]][position[1]].getType()

def monsterInteraction(position, map):
    a = raw_input("""
                You have encountered el Gallo de Oro, how will you prepare your anus?
                a. Furiously masturbate, never breaking eye contact
                b. Leave the room, crying like a little bitch
                c. Defecate on the floor to assert your dominance
                d. none of the above
                e. all of the above
                f. secret answer ;)
                --> """)
    return "Your butthole is now open for business!" if (a.upper() != "F") else "I'm not angry, I'm just disappointed"

def keyInteraction(position, map):
    return "You found a key!"

def generateHardMap():
    blank = Room(0, genericInteraction) # blank room, theoretically never used
    hall = Room(1, genericInteraction) # hallway / passage
    monster = Room("M", monsterInteraction)

    key = Room("Key", keyInteraction)

    return [
    [copy.copy(hall),copy.copy(hall),copy.copy(hall),copy.copy(hall),copy.copy(blank),copy.copy(blank),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(blank),copy.copy(monster),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(hall),copy.copy(hall),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(blank),copy.copy(blank),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(blank),copy.copy(blank),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(blank),copy.copy(blank),copy.copy(blank)],
    [copy.copy(blank),copy.copy(blank),copy.copy(blank),copy.copy(hall),copy.copy(hall),copy.copy(hall),copy.copy(hall)]
    ]

class Room():
    def __init__(self, identifier, interaction):
        self.identifier = identifier
        self.getInteraction = interaction # function returns a string for the user to interact with

    def __str__(self):
        return "0" if self.identifier == 0 else str(self.identifier)

    def getType(self):
        if(self.identifier == 0):
            return "blank"
        elif(self.identifier == 1):
            return "passage"
        elif(self.identifier != "monster"):
            return "item"
        else:
            return "monster"

startingText = """
Welcome to the Gallows de Gallo

You are a weary traveler with a tender butthole, and your mission is to
avert crisis and reach the end of the passageway before your puckerhole
becomes the plaything of a twelve inch burrito. Have fun!

Type 'help' if you're confused at any point."""

# print randomInteraction()