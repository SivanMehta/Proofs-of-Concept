##
## visualizing the last tournemant bracket from http://what-if.xkcd.com/105/
##

import math

population = 7000000000
rounds = int(math.log(population, 2)) + 1

print "population =", population
print "rounds =", rounds

total = 0

for x in xrange(1,rounds + 1):
    print "round %d: %d people die" % (x, 2 ** (rounds - x))
    total += 2 ** (rounds - x)