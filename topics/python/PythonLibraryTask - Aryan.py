# NumPy
# Q1: Given a 2D NumPy array A of shape (5, 5), subtract the mean of each row from every element in that row without using a loop.
# Q2: You have a NumPy array of integers from 1 to 1000. Return a new array containing only the numbers that are divisible by both 3 and 7 but not by 5.
# Q3: Create an 8x8 NumPy array with a chessboard pattern (alternating 0s and 1s), where the top-left element is 0.

import numpy as np
a = np.array([
    [3,8,6,4,8],
    [4,5,6,10,6],
    [17,2,31,8,9],
    [23,34,4,6,16],
    [20,12,10,3,4]])

a_processed = a - np.mean(a,axis=1,keepdims=True)
print(a_processed)

sample = np.arange(1,1001)
b = sample[(sample % 3 == 0) & (sample % 7 == 0) & (sample % 5 != 0)]
print(b)

chessboard = np.zeros((8,8), dtype=int)
chessboard[::2,1::2] = 1
chessboard[1::2,::2] = 1
print(chessboard)