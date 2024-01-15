
import math


def trouver_disposition(N):
    i = 1
    j = 1
    disposition = []
    for i in range(N):
        for j in range(N):
            if math.gcd(i, j) == 1 and i+j <= N and i > 0 and j > 0:
                disposition.append((i, j))
    return disposition


print(trouver_disposition(100))
print(len(trouver_disposition(100)))

disposition = trouver_disposition(100)
res = []
for dispo in disposition:
    a = dispo[0]
    b = dispo[1]
    for c in range(0, a+1):
        for d in range(0, b+1):
            if (a*d - b*c == 1 or a*d - b*c == -1) and (d == b or c == a) and d+c <= a+b:
                if (c, d) not in res:
                    res.append((c, d))
print(len(res))
