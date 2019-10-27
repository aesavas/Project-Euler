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
"""

#1 week - 7 days
#1900 - 1901 --> 365 days
#We need to find 1901 to 2000 so, firstly we have to find that  which day is 1 Jan 1901?
# Year 1900 is in 19th century so, it is divisible by 4 but 19th century is not divisible by 400
# First leap year in 20th century is 1904.

daysOfWeek = 7
namesOfDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysOfYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sumOfDays = 1
sumOfSundays = 0
# 1 Jan 1901 --> Tuesday
firstDayOfCentury = namesOfDays[1]
for i in range(1901, 2001):
    if i % 4 == 0:
        for j in range(0, 12):
            sumOfDays += daysOfLeapYear[j]
            if sumOfDays % daysOfWeek == 6:
                sumOfSundays += 1
    else:
        for j in range(0, 12):
            sumOfDays += daysOfYear[j]
            if sumOfDays % daysOfWeek == 6:
                sumOfSundays += 1
print("Sum Of Sundays the first of the month between 1 Jan 1901 and 31 Dec 2000 : ", sumOfSundays)



