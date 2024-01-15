def nb_digits(n, base):
    if n < 0:
        raise "entier naturel pls"
    if n == 0:
        return 0
    i = 1
    while n > 1:
        n = n//base
        i = i+1
    return i


def convert(n, base):
    if n < 1:
        return ""
    return convert(n//base, base) + str(n % base)


def convert_mirror(n, base):
    if n < 1:
        return ""
    return str(n % base) + convert(n//base, base)


print(nb_digits(1, 10))
print(nb_digits(10, 10))
print(nb_digits(100, 10))
print(nb_digits(0, 10))

print(nb_digits(3, 3))

print(convert(123, 7))
