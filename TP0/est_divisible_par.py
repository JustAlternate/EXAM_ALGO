def somme(n: float) -> float:
    return n*(n+1)/2


print(somme(3.))


def est_divisible_par(n: int, k: int) -> bool:
    return (n % k) == 0


print("Testing est_divisible_par")
print(est_divisible_par(5, 3))
print(est_divisible_par(6, 2))
print(est_divisible_par(9, 3))


def est_pair(n: int) -> bool:
    est_divisible_par(n, 2)
