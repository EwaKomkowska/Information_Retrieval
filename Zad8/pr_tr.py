import numpy as np

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
#L = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],
#              [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

ITERATIONS = 100


def printed(pr):
    pr1 = list(pr)
    pr1.sort(reverse=True)

    sum = 0
    for elem in pr1:  # wyswietlenie danych
        index = pr.index(elem) + 1
        if sum == 0:
            try:
                index = pr.index(elem, index) + 1
                print(index, ':', elem)
                sum += 1
            except:
                print(index, ':', elem)
                sum = 0
        else:
            print(index, ':', elem)
        # w przeciwnym kolejny index


def trustRank(M, d, q):
    previous = list(d)
    for _ in range(0, ITERATIONS):
        trustArray = np.zeros([10], dtype=float)  # wyzerowac array
        for j in range(10):
            trustArray[j] += q * d[j]
            for k in range(10):
                trustArray[j] += (1 - q) * M[j][k] * previous[k]
        previous = list(trustArray)

    sum = 0
    for elem in previous:
       sum += elem

    return previous/sum


def pagerank(M, array, q):
    for i in range(0, ITERATIONS):
        if i != 0:
            previous = list(array)      #bo inaczej wskaznik
            array = np.zeros([10], dtype=float)     #wyzerowac array
            for j in range(10):
                for k in range(10):
                    array[j] += M[j][k] * previous[k]
                array[j] = q + (1 - q) * array[j]
        else:
            for j in range(10):
                array[j] = 1/10            #liczba wierzcholkow

    return previous/sum(previous)


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
pr = np.zeros([10], dtype=float)
pr = list(pagerank(M, pr, q))
printed(pr)
    
### TODO 3: compute trustrank with damping factor q = 0.15
### Documents that are good = 1, 2 (indexes = 0, 1)
### Then, sort and print: (page index (first index = 1, add +1) : trustrank)
### (use regular array + sort method + lambda function)
print("TRUSTRANK (DOCUMENTS 1 AND 2 ARE GOOD)")
q = 0.15
d = np.zeros([10], dtype=float)

seed = [0, 1]    #potem 0, 1   #indexy stron
sum = 0
for i in range(len(d)):
    if i in seed:
        d[i] = 1
        sum += 1

tr = [v/sum for v in d]
tr = list(trustRank(M, list(tr), q))
printed(tr)
#wykorzystujemy macierz M z zad 1
#d ma miec 1 / liczba good, liczba good podana w zadaniu

### TODO 4: Repeat TODO 3 but remove the connections 3->7 and 1->5 (indexes: 2->6, 0->4) 
### before computing trustrank


