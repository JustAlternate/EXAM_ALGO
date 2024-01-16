def tri_bulles(t) :
    n = len(t) #taille de la liste
    i = 0
    permut = True # indicateur de permutation dans la boucle interne
    while (i<n-1) and (permut) :
        j = n-1 #indice du dernier élément
        permut = False
        while j > i:
            if t[j] < t[j-1] : #permutation de 2 éléments
                t[j-1],t[j] = t[j], t[j-1] # on échange les 2 valeurs
                permut = True
            j = j-1
        i = i+1

liste = [1,2,9,5,6,8,4,3,5,9,1,6]
tri_bulles(liste)
print(liste)