#given N x N matrix, write a method to rotate it 90 degree 

import numpy as np


def rotate(mtx):
    new_matrix = np.zeros(mtx.shape)

    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            new_matrix[j, i] = mtx[i, 3-j]
    return new_matrix

def rotate2(mtx):
    N = mtx.shape[0] 
    
    for i in range(int(N/2)):
        for j in range((0+i), (N-i-1)):
            temp = mtx[i][j]  
            mtx[i][j] = mtx[N-1 - j][i] #top = left 
            mtx[N-1-j][i] = mtx[N-1-i][N-1-j] # left = bot
            mtx[N-1-i][N-1-j] = mtx[j][N-1-i] # right = left
            mtx[j][N-1-i] = temp #top = right
        

mtx = np.random.rand(3, 3)
print(mtx)

rotate2(mtx)
print("=======================================")
print(mtx)
