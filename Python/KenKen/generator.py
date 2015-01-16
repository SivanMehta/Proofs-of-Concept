# generates the possibilities given an input in the following form:
# 12x3
# ^^ result of operation
#   ^ operation
#    ^ numbers used
            
def generate(ken, maxNumber): # generates a loop structure to try EVERYTHING
    print ken, ":",

    if(ken[-1] == "1"):
        print ken[:-2]
        return

    result = int(ken[:-2])
    operation = ken[-2]
    loops = int(ken[-1])
    combos = []
    
    loopStatements = []
    for loop in xrange(loops):
        loopStatements.append("for x%d in xrange(1, %d + 1):" % (loop, maxNumber) + "\n" + "\t" * (loop + 1))
        
    loopStructure = ""
    for x in loopStatements:
        loopStructure += x
    
    condition = "if(x0"

    for x in xrange(1, loops):
        condition += " " + operation + " x%d" % x
    condition += " == %d): " % result

    statement = "combos.append(str(x0)"
    for x in xrange(1, loops):
        statement += " + str(x%d)" % x
    condition += statement + ")"

    loopStructure += condition

    # print loopStructure
    exec loopStructure

    # now combos consists of all of the combinations that satisfy the given condition, however, it does contian repeats
    # and we must cleanse them
    trueCombos = []

    s = set()
    if(operation != "*"):
        for combo in combos:
            product = 1
            for number in combo:
                product *= int(number)
            if((product in s) == False):
                trueCombos.append(combo)
                s.add(product)

    else:
        for combo in combos:
            sum = 0
            for number in combo:
                sum += int(number)
            if((sum in s) == False):
                trueCombos.append(combo)
                s.add(sum)


    print trueCombos

generate("8+3", 6)
generate("12*3", 6)