class maillon():
    def __init__(self, val, suiv):
        self.val = val
        self.suiv = suiv

    def free(self):
        pass


class liste_chainee():
    def __init__(self):
        self.taille = 0
        self.tete = None

    def est_vide(self):
        return self.taille == 0

    def sommet(self):
        if not self.taille == 0:
            return self.tete.val

    def ajouter_fin(self, n):
        current = self.tete
        if current is None:
            current = maillon(n, None)

        else:
            while current.suiv is not None:
                current = current.suiv
            current.suiv = maillon(n, None)
        self.taille += 1

    def suppr_index(self, index):
        if not self.est_vide():
            previous = None
            current = self.tete
            for i in range(index):
                previous = current
                current = current.suiv

            if current.suiv is not None:
                previous.suiv = current.suiv

            current.free()
            self.taille -= 1

    def suppr_val(self, val):
        if not self.est_vide():
            prev = self.tete
            cell = prev.suiv
            if prev.val == val:
                self.tete = cell
                return

            while cell is not None:
                if cell.val == val:
                    prev.suiv = cell.suiv
                    cell.free()
                    self.taille -= 1
                    return
                cell = cell.suiv
                prev = prev.suiv

    def __str__(self):
        cell = self.tete
        txt = ""
        while cell is not None:
            txt += str(cell.val)
            cell = cell.suiv
        return txt


L = liste_chainee()
L.ajouter_fin(1)
L.ajouter_fin(2)
L.ajouter_fin(3)
L.ajouter_fin(4)
L.ajouter_fin(5)
L.ajouter_fin(6)
L.suppr_val(4)
print(L)
