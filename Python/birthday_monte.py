# Monte Carlo Simualation of the birthday problem

import random

def birthdayTrial():

    birthdays = set()

    # continually add birthdays until you add the same one twice
    while(True):
        before = len(birthdays)

        randomBirthday = random.randint(1, 365)
        birthdays.add(randomBirthday)

        after = len(birthdays)

        if(before == after):
            return after
            # return the number of birthdays you accumulated

frequencyChart = {}
trials = 100000 # arbitrary

for x in xrange(trials):
    people = birthdayTrial()

    if(people in frequencyChart):
        frequencyChart[people] += 1
    else:
        frequencyChart[people] = 1

maxFreq = 0
maxCount = 365

for count in frequencyChart:
    frequency = frequencyChart[count]
    if(frequency > maxFreq):
        maxFreq = frequency
        maxCount = count

    print count, frequencyChart[count]

print "Max -->", maxFreq, "at %d people" % maxCount