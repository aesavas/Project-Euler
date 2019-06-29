"""
author: aesavas

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385 --> 2 means square.
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025 --> 2 means square.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

listOfNumbers = list(range(1, 101)) # We 101 because it goes to 100.
total = 0
squareTotal = 0
for i in listOfNumbers:
    total += i
    squareTotal += i ** 2 # ** means exponent of number
squareNumbersTotal = total ** 2
print("Result : {} - {} = {}".format(squareNumbersTotal, squareTotal, (squareNumbersTotal - squareTotal)))