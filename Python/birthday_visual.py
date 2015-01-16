import matplotlib.pyplot as plt

def chanceOfImpactWithNPeople(x):
    return (365 - x + 1) / (365.0)

p = 1
probs = []

print "people, chance of collision"
for n in xrange(1, 100):
    p *= chanceOfImpactWithNPeople(n)
    print "%2d %f" % (n, 1 - p)
    # people, chance of finding uniques, chance of collision
    probs.append(1 - p)

plt.plot(range(1, 100), probs)
plt.xlabel('people')
plt.ylabel('probability of common birthdays')

plt.show()