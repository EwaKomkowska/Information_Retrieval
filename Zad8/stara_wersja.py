# coding=utf-8
import numpy as np
import numpy.linalg as la
import scipy.linalg as spla
from functools import reduce

#L1  = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L1  = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
L2  = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
#L3  = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
L3  = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
L4  = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L5  = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
L6  = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
L7  = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
L8  = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
L9  = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
L10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

L = np.array([L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
'''
L1 = [0,1,1,1]
L2 = [0,0,1,1]
L3 = [1,0,0,0]
L4 = [1,0,1,0]
L = np.array([L1, L2, L3, L4])'''

ITERATIONS = 100

def getM(L):
    M = np.zeros([10, 10], dtype=float)
    # number of outgoing links
    c = np.zeros([10], dtype=int)
    
    ## TODO 1 compute the stochastic matrix M
    for i in range(0, 10):
        c[i] = sum(L[i])
    
    for i in range(0, 10):
        for j in range(0, 10):
            if L[j][i] == 0: 
                M[i][j] = 0
            else:
                M[i][j] = 1.0/c[j]
    return M
    
print("Matrix L (indices)")
print(L)    

M = getM(L)

print("Matrix M (stochastic matrix)")
print(M)

### TODO 2: compute pagerank with damping factor q = 0.15
### Then, sort and print: (page index (first index = 1 add +1) : pagerank)
### (use regular array + sort method + lambda function)
print("PAGERANK")
q = 0.15
left_matrix = np.array([[0.0 for _ in range(10)] for _ in range(11)])       #przygotowanie macierzy
right_matrix = np.array(np.zeros([11]), dtype=float)

for i in range(0, 11):           #bedzie jeden wiersz wiecej niz zmiennych
    for j in range(0, 10):          #stworzenie współczynnikó macierzy do równań
        if i == j:
            left_matrix[i][j] = 1 - M[i][j]
        elif i == 10:
            left_matrix[i][j] = 1           #suma wszystkich ma byc rowna 1
        else:
            left_matrix[i][j] = -M[i][j]
    if i != 10:
        right_matrix[i] = 0
    elif right_matrix[i] == 0:
        right_matrix[i] = 1

Q, R = la.qr(left_matrix, mode="complete")
v = spla.solve_triangular(R[:10], Q.T[:10].dot(right_matrix), lower=False)
pr = list(map(lambda x: q + (1 - q) * x, v))
pr1 = list(pr)
pr1.sort(reverse=True)

print(left_matrix)
print(right_matrix)


for elem in pr1:           #wyswietlenie danych
    print(pr.index(elem) + 1, ':', elem)


### TODO 3: compute trustrank with damping factor q = 0.15
### Documents that are good = 1, 2 (indexes = 0, 1)
### Then, sort and print: (page index (first index = 1, add +1) : trustrank)
### (use regular array + sort method + lambda function)
print("TRUSTRANK (DOCUMENTS 1 AND 2 ARE GOOD)")

q = 0.15

d = np.zeros([10], dtype=float)

tr = [v for v in d]
    
### TODO 4: Repeat TODO 3 but remove the connections 3->7 and 1->5 (indexes: 2->6, 0->4) 
### before computing trustrank
