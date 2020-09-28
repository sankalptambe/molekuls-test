import typing
import numpy as np
import sys

INT_MAX = 1000000
  
class Rotten:

    def __init__(self, arr):

        self.arr = np.array(tomato_grid)

        # row and column of the grid
        self.R, self.C = self.arr.shape

        # table
        self.table = [[0 for i in range(self.C)] for j in range(self.R)]
         
        # Visited array to keep track of visited nodes
        self.visited = [[0 for i in range(self.C)] for j in range(self.R)]
         
    # returns the minimum distance to any rotten tomato from [i, j] 
    def Distance(self, i, j):
     
        # If i, j lie outside the array
        if (i >= self.R or j >= self.C or i < 0 or j < 0):
            return INT_MAX
     
        # If 0, return INT_MAX
        elif (self.arr[i][j] == 0):
            self.table[i][j] = INT_MAX
            return INT_MAX
     
        # If -1, return from here
        elif (self.arr[i][j] == -1):
            self.table[i][j] = 0
            return 0
     
        # If node already visited
        elif (self.visited[i][j]):
            return INT_MAX
        else:
            # Mark current node as visited
            self.visited[i][j] = 1
     
            # Check all options
            temp1 = self.Distance(i + 1, j)
            temp2 = self.Distance(i - 1, j)
            temp3 = self.Distance(i, j + 1)
            temp4 = self.Distance(i, j - 1)
     
            # extra credit (test)
            temp5 = self.Distance(i - 1, j - 1)
            temp6 = self.Distance(i + 1, j - 1)
            temp7 = self.Distance(i + 1, j + 1)
            temp8 = self.Distance(i - 1, j + 1)

            # Take the minimum of all
            min_value = 1 + min(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8 )
     
            if self.table[i][j] > 0 and self.table[i][j] < INT_MAX:
                if min_value < self.table[i][j]:
                    self.table[i][j] = min_value
            else:
                self.table[i][j] = min_value
     
            self.visited[i][j] = 0
        return self.table[i][j]
 
# returns the minimum time required to rot all the tomatoes
def main(tomato_grid: typing.List[typing.List[int]]):
   
    t = Rotten(tomato_grid)
    
    max = 0

    # Calculate the minimum distances to any rotten tomato from all the fresh tomatoes
    for i in range(t.R):
        for j in range(t.C):
            if (t.arr[i][j] == 1):
                t.Distance(i,j)
 
    # Pick the maximum distance of fresh tomato to some rotten tomato
    for i in range(t.R):
        for j in range(t.C):
            if (t.arr[i][j] == 1 and
                    t.table[i][j] > max):
                max = t.table[i][j]
 
    # If all tomatoes can be rotten
    if (max < INT_MAX):
        return max
    return -1

if __name__ == "__main__":

    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [1, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]

    assert (main(tomato_grid) == 2), "Tomatoes will be rotten in 2 days"

    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [0, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]

    assert (main(tomato_grid) == -1), "All tomatoes cannot be rotten"
