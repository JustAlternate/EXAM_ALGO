######### EXO 1 ##########

def printTree(self):
    if self.root:
        print(self.root.data)
        if self.root.gauche:
            self.root.gauche.printTree()
        if self.root.droite:
            self.root.droite.printTree()

class Node:

    def __init__(self,data, gauche=None, droite=None):
        self.data = data
        self.gauche = gauche
        self.droite = droite

class terminalNode:

    def __init__(self):
        self.Node = None

class BinaryTree:

    def __init__(self,root=None):
        self.root = root

    def isEmpty(self):
        return self.root == None

    def get_root(self):
        return self.root

    def printTree(self):
        if self.root:
            print(self.root.data)
            if self.root.gauche:
                self.root.gauche.printTree()
            if self.root.droite:
                self.root.droite.printTree()

    def Prefixe(self,res=None):
        if res is None:
            res = []
        if self.root:
            res.append(self.root.data)
            if self.root.gauche :
                self.root.gauche.Prefixe(res)
            if self.root.droite:
                self.root.droite.Prefixe(res)
        return res

    def Infixe(self,res=None):
        if res is None:
            res = []
        if self.root:
            if self.root.gauche:
                self.root.gauche.Infixe(res)
            res.append(self.root.data)
            if self.root.droite:
                self.root.droite.Infixe(res)
        return res

    def Sufixe(self,res = None):
        if res is None:
            res = []
        if self.root:
            if self.root.gauche:
                self.root.gauche.Sufixe(res)
            if self.root.droite:
                self.root.droite.Sufixe(res)
            res.append(self.root.data)
        return res

    def get_type(self):
        return type(self.root.droite)

    def terminal(self):
        if self.root:
            if self.root.gauche is None and self.root.droite is None:
                print(self.root.data)
                self.root.gauche = terminalNode()
                self.root.droite = terminalNode()
            else:
                if self.root.gauche:
                    self.root.gauche.terminal()
                if self.root.droite:
                    self.root.droite.terminal()

    def height(self):
        if self.root is None:
            return None
        else:
            height_left = self.root.gauche.height() if self.root.gauche else 0
            height_right = self.root.droite.height() if self.root.droite else 0
            return 1 + max(height_left,height_right)

    def size(self):
        if self.root is None:
            return None
        else :
            size_left = self.root.gauche.size() if self.root.gauche else 0
            size_right = self.root.droite.size() if self.root.droite else 0
            return 1 + size_left + size_right

    def isEqual(self,a):
        if self.Infixe() == a.Infixe():
            return True
        return False

    def isHeap(self):
        if self.root :
            if self.root.droite :
                if self.root.droite.root.data < self.root.data :
                    return self.root.droite.isHeap()
                else :
                    return False
            if self.root.gauche:
                if self.root.droite.root.gauche.data > self.root.data:
                    return self.root.gauche.isHeap()
                else:
                    return False
        return True

    # def lca(self,a: int, b: int) :
    #     """Return the lowest ancestor commun between two nodes of the tree"""
    #     Racine_a = 0
    #     Racine_b = 0
    #     if self.root is None:
    #         return "Empty tree"
    #
    #     if self.root.gauche:
    #         if self.root.gauche.root.data == a:
    #             Racine_a = self.root.data
    #         elif self.root.gauche.root.data == b:
    #             Racine_b = self.root.data
    #
    #     if self.root.droite:
    #         if self.root.droite.root.data == a:
    #             Racine_a = self.root.data
    #         elif self.root.droite.root.data == b:
    #             Racine_b = self.root.data
    #
    #     return Racine_a,Racine_b

    def lca(self, a: int, b: int) -> Node: ########### A REVOIR NE FONCTIONNE PAS PARFAITEMENT
        """Return the lowest common ancestor between two nodes of the tree"""
        # Si la racine est vide ou égale à a ou b, on la retourne
        if self.root is None or self.root.data == a or self.root.data == b:
            return self.root.data
        # Sinon, on cherche récursivement l'ancêtre commun dans les sous-arbres gauche et droit

        droite = BinaryTree.lca(self.root.droite, a, b) if self.root.droite else None
        gauche = BinaryTree.lca(self.root.gauche, a, b) if self.root.gauche else None

        # Si on trouve a dans un sous-arbre et b dans l'autre, alors la racine est l'ancêtre commun
        if gauche and droite:
            return self.root.data
        # Sinon, on retourne le sous-arbre qui contient l'ancêtre commun, ou None si aucun n'existe
        return gauche or droite

    def isBst(self):
        if self.root is None:
            return True
        else :
            if self.root.gauche :
                if self.root.gauche.root.data < self.root.data:
                    return BinaryTree.isBst(self.root.gauche)
                else :
                    return False
            if self.root.droite :
                if self.root.droite.root.data > self.root.data:
                    return BinaryTree.isBst(self.root.droite)
                else:
                    return False


    def RechercheABR(self,x):
        if not self.root:
            return None
        if x == self.root.data:
            return self.root.data
        elif x < self.root.data:
            return BinaryTree.RechercheABR(self.root.gauche,x)
        else:
            return self.root.droite.RechercheABR(x)

    def ajoutABR(self, x):
        ndx = Node(x, BinaryTree(), BinaryTree())
        if not self.root:
            self.root = ndx
        else:
            current = self
            # descente jusqu'a la feuille
            while current.root is not None:
                pere = current
                if x <= current.root.data:
                    current = current.root.gauche
                else:
                    current = current.root.droite
            # test pour savoir si on ajoute à gauche ou a droite
            if x <= pere.root.data:
                pere.root.gauche = BinaryTree(ndx)
            else:
                pere.root.droite = BinaryTree(ndx)



binary_tree = BinaryTree(Node(2, BinaryTree(Node(1, BinaryTree(Node(0, None, None)), None)), BinaryTree(Node(4, BinaryTree(Node(3, None, None)), BinaryTree(Node(5, None, None))))))

research_binary_tree = BinaryTree(Node(6, BinaryTree(Node(2, BinaryTree(Node(1)), BinaryTree(Node(4, BinaryTree(Node(3)))))), BinaryTree(Node(11, BinaryTree(Node(7)), BinaryTree(Node(12, BinaryTree(Node(12)), BinaryTree(Node(14))))))))
research_binary_tree_2 = BinaryTree(Node(6, BinaryTree(Node(2, BinaryTree(Node(1, None, None)), BinaryTree(Node(4, BinaryTree(Node(3, None, None)), None)))), BinaryTree(Node(11, BinaryTree(Node(7, None, None)), BinaryTree(Node(12, BinaryTree(Node(12, None, None)), BinaryTree(Node(14, None, None))))))))

heap_binary_tree = BinaryTree(Node(5, BinaryTree(Node(3, BinaryTree(Node(0)))), BinaryTree(Node(4, BinaryTree(Node(2)), BinaryTree(Node(1))))))

#printTree(research_binary_tree)
# print(research_binary_tree.height())
# print(research_binary_tree.size())
#print(research_binary_tree.isBst())
# print(binary_tree.root.data)
# print(research_binary_tree.Prefixe())
# print(research_binary_tree.Infixe())
# print(research_binary_tree.Sufixe())
# print(research_binary_tree.RechercheABR(11))
# print(research_binary_tree_2.isEqual(research_binary_tree))
print(heap_binary_tree.isHeap())

print(heap_binary_tree.lca(0,1 ))

#research_binary_tree.ajoutABR(8)




#print(binary_tree.isEqual(research_binary_tree))




# type de self.root.gauche.data --> int
# type de self.root.gauche --> BinaryTree
# type de self.root --> Node
# type de self --> BinaryTree
















########## EXO 1 ##########

# def printTree(self):
#     if self.root:
#         print(self.root.data)
#         if self.root.gauche:
#             self.root.gauche.printTree()
#         if self.root.droite:
#             self.root.droite.printTree()
#
# class Node:
#
#     def __init__(self,data, gauche, droite):
#         self.data = data
#         self.gauche = gauche
#         self.droite = droite
#
# class terminalNode:
#
#     def __init__(self):
#         self.Node = None
#
# class BinaryTree:
#
#     def __init__(self, nodes: list[int | None] | None = None):
#         self.root = self.build_tree(nodes) if nodes else None
#
#     def build_tree(self, nodes_n: list[int | None] | None):
#         if nodes_n is None or not nodes_n:
#             return None
#
#         data = nodes_n[0]
#         gauche = self.build_tree(nodes_n[1::2])
#         droite = self.build_tree(nodes_n[2::2])
#
#         return Node(data, gauche, droite)
#
#     def isEmpty(self):
#         return self.root == None
#
#     def get_data_root(self):
#         return self.root.data
#
#     def get_data_gauche(self):
#         return self.root.gauche.data
#
#     def get_type(self):
#         return type(self)
#
#     def _size(self, node=None) -> int:
#         if node is None:
#             node = self.root
#
#         if node is None:
#             return 0
#
#         return 1 + self._size(node.gauche) + self._size(node.droite)
#
#
#     def print_tree(self, node=None, level=0, prefix="Root: "):
#         if node is None:
#             node = self.root
#
#         if node is not None:
#             print(" " * (level * 4) + prefix + str(node.data))
#             if node.gauche is not None or node.droite is not None:
#                 self.print_tree(node.gauche, level + 1, "Gauche: ")
#                 self.print_tree(node.droite, level + 1, "Droite: ")
#
#     # def height(self) -> int:
#     #     if self.root is None:
#     #         return None
#     #     else:
#     #         height_left = self.gauche.height()
#     #         height_right = self.droite.height()
#     #         return 1 + max(height_right,height_left)
#
# t = [2, 1, 4, 0, None, 3, 5]
# binary_tree_1 = BinaryTree(t)
# binary_tree_1.print_tree()
# print(binary_tree_1.isEmpty())


# type de self.root.gauche.data --> int
# type de self.root.gauche --> Node
# type de self.root --> Node
# type de self --> BinaryTree
