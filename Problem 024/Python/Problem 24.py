"""
author : aesavas

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic
order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

listOfDigit = "0123456789"
permutationNum = 1000000
permutationNum -= 1 #Minus 1, because the first lexicographic number is 0123456789
answer = ""

while listOfDigit:
    factor = math.factorial(len(listOfDigit) - 1)
    print("Factorial : ", factor)
    number = permutationNum // factor
    print("Index : ", number)
    answer += listOfDigit[number]
    print("Out : ", answer)
    permutationNum %= factor
    print("Permution of Number : ", permutationNum)
    listOfDigit = listOfDigit[0: number:] + listOfDigit[number + 1::]#means remove used digit
    print("Digits : ", listOfDigit)
    print("-------------------")

print(answer)