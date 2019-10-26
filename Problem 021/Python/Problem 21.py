"""
author : aesavas

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
start = time.time()

def sumOfDivisors(number):
    return 1 + sum(i + number // i for i in range(2, int(number ** 0.5)+1) if number % i == 0)

# Both functions do same thing. The above is the short version.
"""
def sumOfDivisors(number):
    divisorSum = 0
    for i in range(1, number):
        if number % i == 0:
            divisorSum += i
    return divisorSum
"""

listOfNumbers = list()
sumOfAmicableNumbers = 0
for i in range(1, 10000):
    listOfNumbers.append([i, sumOfDivisors(i)])
print("List is created.")
while len(listOfNumbers) != 0:
    i = listOfNumbers.pop(0)
    for j in listOfNumbers:
        if i[0] == j[1] and i[1] == j[0]:
            sumOfAmicableNumbers += (i[0]+i[1])
            listOfNumbers.remove(j)
            break

print("Sum of all amicable numbers : ", sumOfAmicableNumbers)
print("Time : ", time.time()-start)