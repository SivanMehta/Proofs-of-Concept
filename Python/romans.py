numerals = dict()
numerals["O"] = 0
numerals["I"] = 1
numerals["V"] = 5
numerals["X"] = 10
numerals["L"] = 50
numerals["C"] = 100
numerals["D"] = 500
numerals["M"] = 1000

decimals = dict()
decimals[1] = "I"
decimals[5] = "V"
decimals[10] = "X"
decimals[50] = "L"
decimals[100] = "C"
decimals[500] = "D"
decimals[1000] = "M"

def romanToDecimal(roman):
    if(roman in numerals.keys()):
        return numerals[roman]

    roman = roman.upper() + "O"
    sum = 0
    for index in xrange(len(roman) - 1):
        if(numerals[roman[index]] >= numerals[roman[index + 1]]):
            sum += numerals[roman[index]]
        else:
            sum -= numerals[roman[index]]

    return sum
