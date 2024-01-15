def is_comb_already(comb, Jours, index_J):
    for elem in Jours[index_J]:
        for a in elem:
            if a in comb:
                return False
    return True


def combinaison(nbr_equipe):
    L = []
    for i in range(1, nbr_equipe+1):
        for j in range(1, nbr_equipe+1):
            if (i, j) not in L and (j, i) not in L and i != j:
                L.append((i, j))

    print(L)

    Jours = {1: []}
    index_J = 1
    index = 0

    while L != []:

        if len(Jours[index_J]) == 3:
            index_J += 1
            Jours[index_J] = []

        if is_comb_already(L[index], Jours, index_J):
            Jours[index_J].append(L.pop(index))
        else:
            index = index + 1 % len(L)-1

    return Jours


print(combinaison(6))
