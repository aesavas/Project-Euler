"""
author: aesavas

Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divible1to20():
    listOfNumbers = list(range(2, 21)) # range(2, 21) means 2-20. If we put 20, it goes just 19.
    factorList = list() # It collect factors of numbers
    numberOfFloor = 0   #
    factor = 2
    LSD = 1
    while True:
        notDivible = 0
        for i in range(0, len(listOfNumbers)):
            if(listOfNumbers[i] % factor == 0):
                listOfNumbers[i] /= factor
                if(listOfNumbers[i] == 1):
                    numberOfFloor += 1
            else:
                notDivible += 1
        if(notDivible == len(listOfNumbers)):
            factor += 1
        else:
            factorList.append(factor)
        if numberOfFloor == len(listOfNumbers):
            break
    for i in factorList:
        LSD *= i
    print("{} is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20".format(GSD))

"MAIN :"
divible1to20()

