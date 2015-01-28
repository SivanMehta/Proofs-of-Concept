import copy
from pokedata import *

def lookup(pokemon): return livingDex[pokeIndeces[pokemon]]

"""
    to determine a "defensive score", we will multiply the damage modifiers
    by the number of neutralities, or simply use this logic:

    x4 resistance -> .25
    x2 resistance (normal) -> .5
    neutrality --> 1
    x2 weakness -> 2
    x4 weaknesses -> 4

    for example:
    Blissey (Normal type) has 1 weakness (Fighting), 1 immunity (Ghost), no resistances, and 16 neutralities
    2 * 1 ^ 16 = 2
"""

def getDefensiveScore(pokemon):
    if(type(pokemon) == str):
        pokemon = lookup(pokemon)

    score = 18.0 - len(pokemon.immunities) # there are 18 types

    for pokeType in pokemon.resistances:
        if(pokeType[-1] == 2): # indication of a double resistance
            score *= .25
        else:
            score *= .5
    
    for pokeType in pokemon.weaknesses: # indication of a double weakness
        if(pokeType[-1] == 2):
            score *= 4
        else:
            score *= 2

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
    print "Score --> ", str(minScore)

"""
    to determine an "offensive score", we will simply get the combination that has
    the fewest number of resists
"""

# returns the score with 
def resistsSTAB(attacker, defender):
    return defender.resists(attacker.type1) and defender.resists(attacker.type2)

def getOffensiveScore(attacker):
    if(type(attacker) == str):
        attacker = lookup(attacker)

    score = len(livingDex)

    for defender in livingDex:
        if(resistsSTAB(attacker, defender)):
            score -= 1

    return score

#determining the best possible STAB combo
def findTheoreticalSTAB():
    maxScore = 0 # if every poke resisted (impossible)
    ditto = None

    for pokeType1 in pokeTypes:
        for pokeType2 in pokeTypes:
            minDitto = Pokemon("pokeKiller", pokeType1, pokeType2)
            score = getOffensiveScore(minDitto)

            if(score > maxScore):
                ditto = minDitto
                maxScore = score

    print ditto
    print "Non-Resistors: ", maxScore

def findRealSTAB():
    maxScore = 0
    maxDitto = None

    for pokemon in livingDex:
        score = getOffensiveScore(pokemon)

        if(score > maxScore):
            maxDitto = pokemon
            maxScore = score

    print maxDitto 
    print "Pokemon that don't resist: ", maxScore

def test():
    print """
                                        .::.
                                  .;:**'
                                  `                   
      .:XHHHHk.              db.   .;;.     dH  MX    
    oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN
    QMMMMMb  "MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM
      `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP
       'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM
        ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP
         ?MMM>  YMMMMMM! MM   `?MMRb.    ````   !L"MMMMM XM IMMM
          MMMX   "MMMM"  MM       ~%%:           !Mh.``` dMI IMMP
          'MMM.                                             IMX
           ~M!M                                             IMP"
    """

    print "\n#########################################"
    print "## Getting example defensive scores... ##"
    print "#########################################"
    print lookup("Jigglypuff"), "\nScore --> ", getDefensiveScore("Jigglypuff")
    print lookup("Abomasnow"), "\nScore --> ", getDefensiveScore("Abomasnow")
    print lookup("Aegislash"), "\nScore --> ", getDefensiveScore("Aegislash")

    print "\n######################################################"
    print "## Finding best theoretical defensive type combo... ##"
    print "######################################################"
    findTheoreticalWall()

    print "###################################################"
    print "## Finding best existing defensive type combo... ##"
    print "###################################################"
    findRealWall()

    print "\n#########################################"
    print "## Getting example offensive scores... ##"
    print "#########################################"
    print lookup("Houndoom"), "\nNon-Resistors: ", getOffensiveScore("Houndoom"), "/", len(livingDex)
    print lookup("Xerneas"), "\nNon-Resistors: ", getOffensiveScore("Xerneas"), "/", len(livingDex)
    print lookup("Garchomp"), "\nNon-Resistors: ", getOffensiveScore("Garchomp"), "/", len(livingDex)

    print "\n######################################################"
    print "## Finding best theoretical offensive type combo... ##"
    print "######################################################"
    findTheoreticalSTAB()

    print "\n###################################################"
    print "## Finding best existing offensive type combo... ##"
    print "###################################################"
    findRealSTAB()

    print "\n#######################################"
    print "## Calculating the 'Average Pokemon' ##"
    print "#######################################"

    scores = []
    for pokemon in livingDex:
        scores.append(getDefensiveScore(pokemon))
    defensiveScore = sum(scores) / len(scores)

    for pokemon in livingDex:
        scores.append(getOffensiveScore(pokemon))
    offensiveScore = sum(scores) / len(scores)

    print "Average Defensive Score -> ", defensiveScore
    print "Average Offensive Score -> ", offensiveScore

test()