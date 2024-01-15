class file():
    def __init__(self):
        self.L = []

    def is_Empty(self):
        return self.L == []

    def front(self):
        if not self.is_Empty():
            return self.L[0]
        else:
            raise "Error liste vide"

    def rear(self):
        if not self.is_Empty():
            return self.L[-1]
        else:
            raise "Error liste vide"

    def taille(self):
        return len(self.L)

    def defiler(self):
        if not self.is_Empty():
            return self.L.pop(0)
        else:
            raise "Error liste vide"

    def enfiler(self, n):
        self.L.append(n)
