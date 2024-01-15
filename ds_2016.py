# Exercice 1
from math import sqrt


# Q1.1 ## A RECHECK
def pi(n=0, deno=1):
    if n != 0:
        deno = sqrt(2 + (deno if deno != 1 else 0))

    if (2 / deno) <= (1 + 10**-15):
        return 1

    return (2 / deno) * pi(n + 1, deno)


print(pi())

# Q1.2 - GOOD
p1 = [
    "que",
    "j",
    "aime",
    "à",
    "faire",
    "apprendre",
    "ce",
    "nombre",
    "utile",
    "aux",
    "sages",
]
p2 = [
    "Immortel",
    "Archimède",
    "artiste",
    "ingénieur",
    "qui",
    "de",
    "ton",
    "jugement",
    "peut",
    "priser",
    "la",
    "valeur",
]


def poemeDePi(li: list[str]):
    pi = 0
    for elt in range(0, len(li)):
        if len(li[elt]) < 10:
            pi += len(li[elt]) * (10 ** (-elt))
    return pi


# print(poemeDePi(p1+p2))


# Q2.1
def check_lower(c: str) -> bool:
    return ord(c) >= 97 and ord(c) <= 122


# Q2.2
def count_lower(text: list[str]) -> int:
    li = []
    for word in text:
        count = 0
        for c in word:
            if check_lower(c):
                count += 1
        li.append(count)
    return li


# Q3.1
def moyec(tab: list[int]):
    n = len(tab)
    s = 0
    s_carre = 0

    for elt in tab:
        s += elt
        s_carre += elt**2

    moy = s / n
    ec_carre = (1 / n) * s_carre - moy**2
    ec = sqrt(ec_carre)

    return moy, ec


# Q3.2
def ack(m, n):
    if m == 0:
        return n + 1

    elif m != 0 and n == 0:
        return ack(m - 1, 1)

    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    return None
