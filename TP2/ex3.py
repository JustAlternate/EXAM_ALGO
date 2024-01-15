def fibo(n, dico={}):
    if n < 0:
        raise "gros nul"
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n-1 not in dico:
        dico[n-1] = fibo(n-1, dico)
    if n-2 not in dico:
        dico[n-2] = fibo(n-2, dico)
    return dico[n-1] + dico[n-2]


def fibo_ite(n):
    fib0 = 0
    fib1 = 1
    total = 0
    if n == 0:
        return fib0
    elif n == 1:
        return fib1
    while n-1:
        total = fib1 + fib0
        n -= 1
        fib0 = fib1
        fib1 = total

    return total


def affiche_fibo(n):
    for i in range(n):
        print(fibo(i))


print(fibo(10))
print(fibo_ite(10))
print("====")
print(affiche_fibo(100))
