class Tree:
    def __init__(self, val):
        self.val = val
        self.g = None
        self.d = None

    def add_g(self, val) -> None:
        if self.g is None:
            self.g = Tree(val)
        else:
            assert ("Cant, g already exist")

    def add_d(self, val) -> None:
        if self.d is None:
            self.d = Tree(val)
        else:
            assert ("Cant, d already exist")

    def height(self) -> int:
        if self.val is None:
            return -1
        if self.d is not None and self.g is not None:
            return max(self.d.height() + 1, self.g.height() + 1)
        if self.d is not None:
            return self.d.height() + 1
        if self.g is not None:
            return self.g.height() + 1
        return 0

    def size(self) -> int:
        if self.val is None:
            return 0
        if self.g is None and self.d is None:
            return 1
        if self.d is not None:
            a = self.d.size()
        if self.g is not None:
            b = self.g.size()
        return a+b+1

    def isEmpty(self) -> bool:
        return self.g is None and self.d is None


A = Tree(1)
A.add_d(2)
A.add_g(1)
print(A.height())
print(A.size())
