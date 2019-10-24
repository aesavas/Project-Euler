"""
author : aesavas

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import time

start = time.time()

grid_size = 20
lst = [[0 for x in range(0, grid_size)] for y in range(0, grid_size)]
print(lst)
for col in range(0, grid_size):
        lst[0][col] = col+2
for row in range(0, grid_size):
        lst[row][0] = row+2
for row in range(1, grid_size):
    for col in range(1, grid_size):
        lst[row][col] = lst[row][col-1] + lst[row-1][col]
print(lst)
print ("Number of routes for a {0}x{0} size grid: {1}".format(grid_size, lst[grid_size-1][grid_size-1]))


print(time.time() - start)
