# This code uses recursion to get an answer.
# The sudoku grid must have at least 16 numbers to have a solution

import numpy as np

grid = [
    [0,6,9,0,0,8,0,0,2],
    [2,5,8,0,0,9,1,3,7],
    [7,0,0,0,0,0,0,8,6],
    [0,3,4,9,0,1,0,0,5],
    [1,9,2,5,0,4,0,6,8],
    [6,0,5,2,8,3,0,0,0],
    [0,8,0,0,0,6,7,5,4],
    [4,2,0,8,0,0,0,0,9],
    [5,0,0,4,9,7,8,0,0]
]

def validPlace(i,j,n):
    global grid
    if n not in grid[i]:
        for k in range(9):
            if grid[k][j]==n:
                return False
        for k in range((i-(i%3)),(i-(i%3))+3):
            for l in range((j-(j%3)),(j-(j%3))+3):
                if grid[k][l]==n:
                    return False
        return True
    return False

def insertNumber(i,j,n):
    global grid
    grid[i][j] = n

def autocomplete():
    global grid
    for i in range(9):
        for j in range(9):
            if(grid[i][j] == 0):
                for k in range(1,10):
                    if(validPlace(i,j,k)):
                        insertNumber(i,j,k)
                        autocomplete()
                        insertNumber(i,j,0)
                return
    print(np.matrix(grid))


autocomplete()
