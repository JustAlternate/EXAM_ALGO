from random import randint


def créer_damier_aleatoire(n, m):
    L = []
    for i in range(n):
        L.append([])
        for j in range(m):
            L[i].append(randint(0, 1))
    return L


L_damier_test = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
]


def robot_cupide(damier: list[list[list]], x: int = 0, y: int = 0) -> int:
    print("Position robot: ", x, y)
    # Si on est tout en bas a droite on sort
    if len(damier)-1 == y and len(damier[0])-1 == x:
        return damier[x][y]

    ligne = [damier[y][i] for i in range(y+1, len(damier))]
    colone = [damier[i][x] for i in range(x+1, len(damier[0]))]

    if sum(colone) > sum(ligne) and y < len(damier)-1:
        return damier[x][y] + robot_cupide(damier, x, y+1)
    elif x < len(damier[0])-1:
        return damier[x][y] + robot_cupide(damier, x+1, y)


print("Bitcoins : ", robot_cupide(L_damier_test, 0, 0))
