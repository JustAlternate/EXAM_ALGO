def triRapide(liste):
    if liste==[]:
        return liste
    liste_g=[]
    liste_d=[]
    for i in range(1,len(liste)):
        if liste[i]<=liste[0]:
            liste_g.append(liste[i])
        else:
            liste_d.append(liste[i])
    return triRapide(liste_g)+[liste[0]]+triRapide(liste_d)


test3 = [1,2,9,5,6,8,4,3,5,9,1,6]
print(triRapide(test3))