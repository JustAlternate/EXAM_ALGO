def tri_insertion(t):
    n = len(t)
    i = 1
    while i < n:
        k = i - 1
        current_value = t[i]

        while (k >= 0) and (t[k] > current_value):
            t[k + 1] = t[k]
            k = k - 1

        t[k + 1] = current_value
        i = i + 1

liste = [1,2,9,5,6,8,4,3,5,9,1,6]
tri_insertion(liste)
print(liste)