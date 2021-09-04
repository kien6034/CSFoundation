#write an algorithm such that if an element in an MxN matrix is zero, its entire row and column are set to zero
import numpy as np

M = 8
N = 6


def find_zero(mtx):
    row = False
    col = False
    for i in range(0, M):
        for j in range(0, N):
            if mtx[i,j] == 0:
                if i == 0:
                    row = True
                if j == 0:
                    col = True 

                mtx[0, j] = 0
                mtx[i, 0] = 0
    return row, col


def zerorize_col(mtx, j):
    for i in range(1, M):
        mtx[i, j] = 0

def zerorize_row(mtx, i):
    for j in range(1, N):
        mtx[i, j] = 0

def zerorize(mtx, row, col):
    for j in range(1, N):
        if mtx[0, j] == 0:
            zerorize_col(mtx, j)

    #second row
    for i in range(1, M):
        if mtx[i, 0] == 0:
            zerorize_row(mtx, i)
    
    if row:
        zerorize_row(mtx, 0)
    if col:
        zerorize_col(mtx,0)

mtx = np.where(np.random.rand(M,N) > 0.2, 4 ,0)
print(mtx)

row, col = find_zero(mtx)
print("=====================")
print(mtx)

zerorize(mtx, row, col)
print("=====================")
print(mtx)