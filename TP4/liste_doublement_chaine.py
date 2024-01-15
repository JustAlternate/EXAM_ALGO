
class Cell:
    def __init__(self, val: int):
        self.val = val
        self.suiv = self
        self.prec = self

    def __str__(self):
        return ("("+str(self.prec.val)+", "+str(self.val)+", "+str(self.suiv.val)+")")


class LinkedList:
    def __init__(self, size=0):
        self.size = size
        self.tete = None
        self.dernier = None

    def IsEmpty(self):
        return self.size == 0

    def append(self, c: Cell):
        if self.size == 0:
            c.prec = c
            c.suiv = c
            self.tete = c
            self.dernier = c
            self.size += 1
            return

        prec = self.tete.prec
        suivant = self.tete.suiv
        while suivant is not self.tete:
            prec = suivant
            suivant = suivant.suiv

        prec.suiv = c
        c.prec = prec
        c.suiv = self.tete
        self.dernier = c
        self.tete.prec = c
        self.size += 1

    def __str__(self):
        text = ""
        text += "size = "+str(self.size)+"\n"
        text += "["+str(self.tete)
        suivant = self.tete.suiv
        while suivant is not self.tete:
            text += str(suivant)
            suivant = suivant.suiv
        text += "]"
        return text


L = LinkedList()
for x in range(10):
    L.append(Cell(x))
print(L)
