"""
author : aesavas

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacciSequence(digit):
    F1 = 1
    F2 = 1
    counter = 3 #because firstly, find 3rd term.
    while True:
        F3 = F1 + F2
        if len(str(F3)) == digit:
            return counter
        F1, F2 = F2, F3
        counter += 1

print("Index of Number : ", fibonacciSequence(1000))