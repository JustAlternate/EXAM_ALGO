import random
import time

# Ex 1


def genere_rand_list(n):
    return [random.randint(0, 10000) for _ in range(n)]


print(genere_rand_list(10))

# Ex 2


def timeAlgo(algo, L):
    start_time = time.time()
    algo(L)
    end_time = time.time()
    print("Complexité en temps d'exec pour n = " + str(len(L)) +
          " t = "+str(end_time - start_time)+" secondes")
    return round(end_time - start_time)


# Ex 4

def tri_insertion(t):
    n = len(t)
    for i in range(1, n):
        k = i-1
        x = t[i]
        while (k >= 0) and (t[k] >= x):
            t[k+1] = t[k]
            k = k-1
        t[k+1] = x
        i += 1


def tri_select(L):
    n = len(L)
    for i in range(n-1):
        j = i
        for k in range(i+1, n):
            if L[k] < L[j]:
                j = k
    L[i], L[j] = L[j], L[i]


def tri_bulle(L):
    n = len(L)
    i = 0
    permut = True
    while (i < n-1) and permut:
        j = n-1
        permut = False
        while j > i:
            if L[j] < L[j-1]:
                L[j-1], L[j] = L[j], L[j-1]
                permut = True
            j -= 1
        i += 1


def tri_fusion(L):
    if len(L) == 1:
        return L

    first = L[:len(L)//2]
    last = L[len(L)//2:]

    first = tri_fusion(first)
    last = tri_fusion(last)

    def merge(first, last):
        new = []
        while len(first) > 0 and len(last) > 0:
            if first[0] > last[0]:
                new.append(last.pop(0))
            else:
                new.append(first.pop(0))

        while len(first) > 0:
            new.append(first.pop(0))
        while len(last) > 0:
            new.append(last.pop(0))

        return new

    return merge(first, last)


def tri_denombrement(L):
    dico = {}
    for elem in L:
        if elem in dico:
            dico[elem] += 1
        else:
            dico[elem] = 1

    print(dico)
    new = []
    for j in range(0, max(L)+1):
        if j in dico:
            for _ in range(dico[j]):
                new.append(j)
    return new


# Ex 3
LL = [genere_rand_list(10**n) for n in range(3, 5)]

LLL = [
]

algos = [
    tri_insertion, tri_select, tri_bulle, tri_fusion, tri_denombrement
]

for L in LL:
    LLL.append([timeAlgo(algo, L) for algo in algos])

print(LLL)
