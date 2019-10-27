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
    if number == 0:
        return 0
    return 1 + sum(i + number // i for i in range(2, int(number ** 0.5)+1) if number % i == 0)

listOfNumbers = list()
sumOfAmicableNumbers = 0
for i in range(0, 10000):
    listOfNumbers.append([i, sumOfDivisors(i)]) #[index number, sum of divisors index number]
print("List is created.")
for i in range(0, 10000):
    result = listOfNumbers[i][1]
    if result < 10001:
        if i == listOfNumbers[result][1] and i != result:
            sumOfAmicableNumbers += i

print("Sum of all amicable numbers : ", sumOfAmicableNumbers)
print("Time : ", time.time()-start)