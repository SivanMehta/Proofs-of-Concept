import copy
from pokedata import *

"""
to determine a "defensive score", we will add up the damage modifiers, or simply use this logic:
immunity -> +0
x4 resistance -> .25
x2 resistance (normal) -> .5
neutrality --> 1
x2 weakness -> 2
x4 weaknesses -> 4

for example:
Blissey (Normal type) has 1 weakness (Fighting), 1 immunity (Ghost), no resistances, and 16 neutralities
2 + 0 + 16 -> 18
"""

def getDefensiveScore(pokemon):

    if(type(pokemon) == str):
        pokemon = livingDex[pokeIndeces[pokemon]]
        print(pokemon)

    # setting score to the amount of neutralities among the 18 types
    score = 18 - len(pokemon.resistances) - len(pokemon.weaknesses) - len(pokemon.immunities)

    for pokeType in pokemon.resistances:
        if(pokeType[-1] == 2): # indication of a double resistance
            score += .25
        else:
            score += .5
    
    for pokeType in pokemon.weaknesses: # indication of a double weakness
        if(pokeType[-1] == 2):
            score += 4
        else:
            score += 2

    return score

# this to determine the lowest score in theory, not in practice
def findTheoreticalWall():
    minScore = 72 # if you were x4 weak to literally every type (impossible)
    minDitto = None

    for pokeType1 in pokeTypes:
        for pokeType2 in pokeTypes:
            megaDitto = Pokemon("pokeWall", pokeType1, pokeType2)
            score = getDefensiveScore(megaDitto)

            if(score < minScore):
                minDitto = megaDitto
                minScore = score

    print(minDitto)
    print("Score --> " + str(minScore) + "\n")

# findTheoreticalWall()

def findRealWall():
    minScore = 72 # if you were x4 weak to literally every type (impossible)
    minDitto = None

    for pokemon in livingDex:
        score = getDefensiveScore(pokemon)

        if(score < minScore):
            minDitto = pokemon
            minScore = score

    print(minDitto)
    print("Score --> " + str(minScore) + "\n")

# findRealWall()

"""
to determine an "offensive score", we will simply get the combination that has
the fewest number of resists
"""

def getOffensiveScore(poketype1, poketype2):
    score = 0

    for pokemon in livingDex:
        if (pokemon.resists(poketype1) or str(poketype1).capitalize() in pokemon.immunities) and ((pokemon.resists(poketype2) or str(poketype2).capitalize() in pokemon.immunities)):
            score += 1

    return score

def findSTAB():
    minScore = 718 # if every poke resisted (impossible)
    megaDitto = None

    for pokeType1 in pokeTypes:
            for pokeType2 in pokeTypes:
                megaDitto = Pokemon("pokeKiller", pokeType1, pokeType2)
                score = getOffensiveScore(megaDitto.type1, megaDitto.type2)

                if(score < minScore):
                    minDitto = megaDitto
                    minScore = score

    print(minDitto)
    print("Resistors: ", minScore)

print(getDefensiveScore("Jigglypuff"))
print(getDefensiveScore("Abomasnow"))
print(livingDex[pokeIndeces["Shuckle"]])
print(livingDex[pokeIndeces["Mawile"]])