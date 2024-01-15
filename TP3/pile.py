from ctypes import Array, c_int


def alloc(m: int) -> Array:
    IntArrayType = c_int * m
    return IntArrayType()

# Exercice 4


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.n = 0
        self.array = alloc(max_size)


def s_new(n: int) -> Stack:
    return Stack(n)


def s_size(s: Stack) -> int:
    return s.n


def s_is_empty(s: Stack) -> bool:
    return s.n == 0


def s_str(s: Stack) -> str:
    string = ""
    for i in range(s.n):
        string += str(s.array[i])
    return "[|"+string+"|]"


def s_push(s: Stack, item: int) -> Stack:
    if s.n >= s.max_size:
        return s
    s.array.append(item)
    return s
