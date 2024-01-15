from math import sqrt
from decimal import Decimal as dec

dico = {
    0: 0,
    1: dec(sqrt(2))
}


def calc(n):
    global dico
    if n in dico:
        return dico[n]
    else:
        dico[n] = dec(sqrt(2+calc(n-1)))
    return dico[n]


def calc_pi(i=1):
    fac = dec(2/calc(i))
    if fac < dec(1+(10**(-15))):
        return 1
    return dec(fac * calc_pi(i+1))


print(2*calc_pi())
