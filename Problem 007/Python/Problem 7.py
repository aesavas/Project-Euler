"""
author: aesavas

Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def isPrimeNumber(number):
    for i in range(2, int(number ** 0.5)+1):
        if(number % i == 0):
            return False
    return True

counter = 1
number = 2
while(counter != 10002):
    if isPrimeNumber(number):
        counter += 1
        number += 1
        #print("Counter : ", counter)
    else:
        number += 1

print("10001st prime number is ", number - 1) # We subtact 1 because we add 1 if else block