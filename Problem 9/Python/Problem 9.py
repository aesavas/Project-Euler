"""
author: aesavas

Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2 --> 2s means square.
For example, 32 + 42 = 9 + 16 = 25 = 52. --> 2s means square.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

total = 1000
for a in range(1, int(total / 3)+1): # 'a' can be maximum 333
    for b in range(a+1, int(total/2)+1): # range must be start a+1 because a < b
        c = total - (a + b)
        if (a ** 2 + b ** 2 == c ** 2):
            print("A : {}\nB : {}\nC : {}".format(a, b, c))
            print("ABC : ", a*b*c)
            a = 333 # because we want to break other for loop
            break

