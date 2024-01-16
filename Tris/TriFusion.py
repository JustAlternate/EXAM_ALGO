def Tri_Fusion(tableau):
    if len(tableau) <= 1:
        return tableau

    milieu = len(tableau) // 2
    gauche = tableau[:milieu]
    droite = tableau[milieu:]

    gauche = Tri_Fusion(gauche)
    droite = Tri_Fusion(droite)

    fusionner(tableau, gauche, droite)

    return tableau

def fusionner(t, gauche, droite):
    index_tableau = 0
    index_gauche = 0
    index_droite = 0

    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] < droite[index_droite]:
            t[index_tableau] = gauche[index_gauche]
            index_gauche += 1
        else:
            t[index_tableau] = droite[index_droite]
            index_droite += 1
        index_tableau += 1

    # Copier les éléments restants de gauche, s'il y en a
    while index_gauche < len(gauche):
        t[index_tableau] = gauche[index_gauche]
        index_gauche += 1
        index_tableau += 1

    # Copier les éléments restants de droite, s'il y en a
    while index_droite < len(droite):
        t[index_tableau] = droite[index_droite]
        index_droite += 1
        index_tableau += 1

liste = [1,2,9,5,6,8,4,3,5,9,1,6]
Tri_Fusion(liste)
print(liste)