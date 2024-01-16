def tri_selection(t) :
    n = len(t) # taille de la liste
    for i in range(n-1) : # recherche du ième plus petit élément
        j = i
        for k in range(i+1,n) :
            if t[k] < t[j] :
                j=k
        t[i], t[j] =t[j], t[i] # échange des deux valeurs

liste = [1,2,9,5,6,8,4,3,5,9,1,6]
tri_selection(liste)
print(liste)