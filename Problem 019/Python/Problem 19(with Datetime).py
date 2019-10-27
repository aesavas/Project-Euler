"""
author : aesavas

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

I don't like this way bu it shortest way for answer.
I will give the another way.
"""
import datetime

sumOfSundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            sumOfSundays += 1

print("Sum Of Sundays the first of the month between 1 Jan 1901 and 31 Dec 2000 : ", sumOfSundays)

#Also, we can do it 1 line.
print("1 Line Answer : ", sum(1 for year in range(1901, 2001) for month in range(1, 13) if datetime.date(year, month, 1).weekday() == 6))