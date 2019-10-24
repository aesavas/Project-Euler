"""
author : aesavas

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time
start = time.time()

listOfChain = [None]*1000000
lengthOfChain = 0
number = 0
counter = 1
while counter < 1000000:
    temp = counter
    tempChain = 0
    while temp > 1:
        if temp % 2 == 0:
            temp = int(temp / 2)
        else:
            temp = 3*temp + 1
        tempChain += 1
        if temp < 1000000:
            if listOfChain[temp] is not None:
                tempChain += listOfChain[temp]
                break
    if tempChain > lengthOfChain:
        lengthOfChain = tempChain
        number = counter
    listOfChain[counter] = tempChain
    counter += 1

print(number," starting number, under one million, produces the longest chain.")
print("Length of chain : ", lengthOfChain)
print("Time : ", time.time() - start)