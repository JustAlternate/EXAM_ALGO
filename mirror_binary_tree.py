class binary_tree():
    def __init__(self, val):
        self.val = val
        self.g = None
        self.d = None

    def add_g(self, val):
        self.g = binary_tree(val)

    def add_d(self, val):
        self.d = binary_tree(val)

    def __str__(self):
        txt = ""
        txt += str(self.val)
        txt += "/\\"
        if self.d is not None:
            txt += str(self.d)
        if self.g is not None:
            txt += str(self.g)
        return txt


def mirror_tree(b: binary_tree) -> binary_tree:
    new_b = binary_tree(b.val)

    def a(b, new_b):
        if b.d is not None:
            new_b.g = b.d
            a(b.d, new_b.g)
        if b.g is not None:
            new_b.d = b.g
            a(b.g, new_b.d)

    a(b, new_b)
    return new_b


b = binary_tree(0)
b.add_d(1)
b.add_g(2)
b.g.add_g(3)
b.d.add_d(4)

print(b)

new_b = mirror_tree(b)

print(new_b)
