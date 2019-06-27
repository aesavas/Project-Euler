"""
author: aesavas

Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def findLargestPrimeFactor(number):
    largest = 0
    factor = 2
    while(number >= factor):
        if( number % factor == 0):
            largest = factor
            number /= factor
        else:
            factor += 1
    print("Largest Prime Factor : ", largest)

findLargestPrimeFactor(600851475143)
