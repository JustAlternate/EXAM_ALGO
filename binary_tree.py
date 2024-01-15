class binary_tree():
    def __init__(self, val):
        self.val = val
        self.g = None
        self.d = None

    def add_g(self, val):
        self.g = binary_tree(val)

    def add_d(self, val):
        self.d = binary_tree(val)


b = binary_tree(0)
b.add_d(1)
b.add_g(2)
b.g.add_g(3)
b.d.add_d(4)
