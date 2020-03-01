"""
author : aesavas

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


if __name__ == "__main__":
    LIMIT = 28124  # Because index of list starts from 0.
    sumOfDivisors = [0] * LIMIT
    for number in range(1, LIMIT):
        # We starts from number * 2. Because we do not want to numbers itself.
        for i in range(number * 2, LIMIT, number):
            sumOfDivisors[i] += number
    abundantNumbers = [index for index,item in enumerate(sumOfDivisors) if item > index]
    # We can accept non abundant numbers that all numbers between 0 and LIMIT
    nonAbundantNumber = [1] * LIMIT
    for i in abundantNumbers:
        for j in abundantNumbers:
            if (i + j) < LIMIT:
                # Then, we allocate abundant numbers from nonAbundantNumber list
                nonAbundantNumber[i + j] = 0
            else:
                break
    # In here, we sum all non abundant numbers between 0 and LIMIT
    print(sum(index for index, item in enumerate(nonAbundantNumber) if item == 1))
