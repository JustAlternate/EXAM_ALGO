import copy
L = [2, 4, 7, 18]


def two_sum_array(L_origin, target):
    L_origin.sort()
    L = copy.deepcopy(L_origin)
    index_min = 0
    while len(L) != 0:
        min = L.pop(0)
        for j in range(0, len(L)):
            if L[j] + min == target:
                return index_min, j+index_min+1
        index_min += 1
    return "No target"


print(two_sum_array(L, 9))


def two_sum_array_dico(L_origin, target):
    L_origin.sort()
    L = copy.deepcopy(L_origin)
    dico = {}
    index = 0
    for elem in L:
        if target-elem in dico:
            return dico[target-elem], index
        dico[elem] = index
        index += 1
    return "No target"


print(two_sum_array_dico(L, 9))
