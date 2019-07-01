"""
author: aesavas

Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
This is the simplest way of solution but it is not good.
Because it takes nearly 2 minutes. So this is lazy code.
I share it because it is the first solution that comes to mind.
"""

def isPrime(number):
    factor = 2
    while factor <= number**0.5:
        if number % factor == 0:
            return False
        factor += 1
    return True


counter = 2
summationOfPrimes = 0
while counter < 2000000:
    if isPrime(counter):
        summationOfPrimes += counter
    counter += 1
print("Summation of primes : ", summationOfPrimes)

