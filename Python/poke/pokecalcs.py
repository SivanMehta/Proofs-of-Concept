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

    print minDitto
    print "Score --> " + str(minScore) + "\n"

def findRealWall():
    minScore = 72 # if you were x4 weak to literally every type (impossible)
    minDitto = None

    for pokemon in livingDex:
        score = getDefensiveScore(pokemon)

        if(score < minScore):
            minDitto = pokemon
            minScore = score

    print minDitto
    print "Score --> " + str(minScore)

"""
to determine an "offensive score", we will simply get the combination that has
the fewest number of resists
"""

def getOffensiveScore(test_pokemon):
    if(type(test_pokemon) == str):
        test_pokemon = livingDex[pokeIndeces[test_pokemon]]
        print(test_pokemon)
    elif(type(test_pokemon) == Pokemon):
        print test_pokemon

    score = 718

    for pokemon in livingDex:
        if (pokemon.resists(test_pokemon.type1) or str(test_pokemon.type1).capitalize() in pokemon.immunities) and ((pokemon.resists(test_pokemon.type2) or str(test_pokemon.type2).capitalize() in pokemon.immunities)):
            score -= 1

    return score

#determining the best possible STAB combo
def findTheoreticalSTAB():
    maxScore = 0 # if every poke resisted (impossible)
    megaDitto = None

    for pokeType1 in pokeTypes:
            for pokeType2 in pokeTypes:
                megaDitto = Pokemon("pokeKiller", pokeType1, pokeType2)
                score = getOffensiveScore(megaDitto)

                if(score > maxScore):
                    minDitto = megaDitto
                    maxScore = score

    print minDitto
    print"Pokemon that don't resist: ", maxScore

def findRealSTAB():
    maxScore = 0
    maxDitto = None

    for pokemon in livingDex:
        score = getOffensiveScore(pokemon)

        if(score > maxScore):
            maxDitto = pokemon
            maxScore = score

    print maxDitto 
    print "Score --> " + str(maxScore) + "\n"

print "\n#########################################"
print "## Getting example defensive scores... ##"
print "#########################################"
print getDefensiveScore("Jigglypuff")
print getDefensiveScore("Abomasnow")
print getDefensiveScore("Steelix")


print "\n#########################################"
print "## Getting example offensive scores... ##"
print "#########################################"
print getOffensiveScore("Houndoom")
print getOffensiveScore("Xerneas")
print getOffensiveScore("Rhyperior")
print getOffensiveScore("Garchomp")

print "\n######################################################"
print "## Finding best theoretical defensive type combo... ##"
print "######################################################"
findTheoreticalWall()

print "###################################################"
print "## Finding best existing defensive type combo... ##"
print "###################################################"
findRealWall()

print "\n######################################################"
print "## Finding best theoretical offensive type combo... ##"
print "######################################################"
findTheoreticalSTAB()

print "\n###################################################"
print "## Finding best existing offensive type combo... ##"
print "###################################################"
findRealSTAB()