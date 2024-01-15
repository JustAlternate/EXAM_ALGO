import math


def facto(n):
    if n < 0:
        raise "Mon gars faut que tu me donnes des val >= 0 bg"
    if n == 0:
        return 1
    return facto(n-1)*n


print(facto(0))
print(facto(3))
print(facto(-1))
