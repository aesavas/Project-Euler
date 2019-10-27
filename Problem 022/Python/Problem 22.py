"""
author : aesavas

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import time
start = time.time()
pointOfAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
file = open("p022_names.txt", "r")
listOfNames = list()
totalNameScores = 0
listOfNames = file.read().split(',')
listOfNames.sort()
for i in range(len(listOfNames)):
    listOfNames[i] = listOfNames[i].replace('"', '')
    temp = 0
    print("Name : ", listOfNames[i], "Place : ", (i + 1))
    for j in range(len(listOfNames[i])):
        indexOfLetter = pointOfAlphabet.index(listOfNames[i][j])
        temp += (indexOfLetter + 1)
    print("Sum of Alphabet Point : ", temp)
    print("Score : ", temp*(i + 1))
    print("-------------------------------------------------------")
    totalNameScores += temp * (i + 1)
print("Total Name Scores : ", totalNameScores)
print("Time : ", time.time()-start)
