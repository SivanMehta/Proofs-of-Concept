import math, random

def generateRandomColor():
    color = "#"
    for x in xrange(3):
        adding = hex( int(random.random() * 255) )[2:] #random number from 0 to 255 convert to hex
        if(len(adding) == 1):
            adding += "0"
        color += adding
    return color

def uniform(*bounds):
    try:
        return random.randint(bounds[0], bounds[1])
    except:
        raise ValueError("Incorrect bounds on Uniform Distribution")