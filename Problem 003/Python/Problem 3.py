"""
author: aesavas

Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def findLargestPrimeFactor(number):
    factor = 2
    while(factor <= int(number ** 0.5)):
        if(number % factor == 0):
            number /= factor
        else:
            factor += 1
    return int(number)


findLargestPrimeFactor(600851475143)
