"""
author : aesavas

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenToTwenty = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
               "nineteen"]
decimal = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
sumOfCharacter = 0  # type: int
for i in numbers + tenToTwenty:
    sumOfCharacter += len(i)
for i in range(20, 1001):
    number = ""
    if i // 1000 != 0:
        number = "onethousand"
        sumOfCharacter += len(number)
        continue
    if i // 100 != 0:
        index = i // 100
        number = numbers[index - 1] + "hundred"
        if (i % 100) // 10 > 1:
            index = (i % 100) // 10
            number += "and" + decimal[index - 2]
            if (i % 100) % 10 > 0:
                index = (i % 100) % 10
                number += numbers[index - 1]
            sumOfCharacter += len(number)
            continue
        elif (i % 100) // 10 == 1:
            index = (i % 100) % 10
            number += "and" + tenToTwenty[index]
            sumOfCharacter += len(number)
            continue
        else:
            index = (i % 100) % 10
            if index > 0:
                number += "and" + numbers[index - 1]
            sumOfCharacter += len(number)
            continue
    else:
        index = (i % 100) // 10
        if index >= 2:
            number = decimal[index - 2]
            if (i % 100) % 10 > 0:
                index = (i % 100) % 10
                number += numbers[index - 1]
            sumOfCharacter += len(number)
            continue

print("Numbers of characters : {}".format(sumOfCharacter))

"""
numbers = ["one","two","three","four","five","six","seven","eight","nine"]
tenToTwenty = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decimal = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
sumOfCharacter = 0
for i in numbers+tenToTwenty:
    sumOfCharacter += len(i)
for i in range(20, 1001):
    number = ""
    if i // 1000 != 0:
        number = "onethousand"
        sumOfCharacter += len(number)
        continue
    if i // 100 != 0:
        index = i // 100
        number = numbers[index - 1] + "hundred"
        if (i % 100) // 10 > 1:
            index = (i % 100) // 10
            number = number + "and" + decimal[index - 2]
            if (i % 100) % 10 > 0:
                index = (i % 100) % 10
                number += numbers[index - 1]
            sumOfCharacter += len(number)
            continue
        elif (i % 100) // 10 == 1:
            index = (i % 100) % 10
            number = number + "and" + tenToTwenty[index]
            sumOfCharacter += len(number)
            continue
        else:
            index = (i % 100) % 10
            if index > 0:
                number = number + "and" + numbers[index - 1]
            sumOfCharacter += len(number)
            continue
    else:
        index = (i % 100) // 10
        if index >= 2:
            number = decimal[index - 2]
            if (i % 100) % 10 > 0:
                index = (i % 100) % 10
                number += numbers[index - 1]
            sumOfCharacter += len(number)
            continue
print("Number of characters : {}".format(sumOfCharacter))
"""