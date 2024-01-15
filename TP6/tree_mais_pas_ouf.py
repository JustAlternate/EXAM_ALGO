from pyglet.math import Vec2


class Node:
    def __init__(self, label, left_node, right_node):
        self.label = label
        self.left_node = left_node
        self.right_node = right_node


class TerminalNode:
    def __init__(self):
        self.label = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self) -> bool:
        return self.root is None

    def root(self) -> Node:
        return self.root

    def height(self) -> int:
        # Vérifie si la racine est un noeud terminal (arbre vide ou feuille)
        if not self.root or isinstance(self.root, TerminalNode):
            return 0

        # Calcul récursif de la hauteur pour chaque sous-arbre
        left_height = self.root.left_node.height() if self.root.left_node else 0
        right_height = self.root.right_node.height() if self.root.right_node else 0

        # Retourne la hauteur maximale des sous-arbres, plus un pour la racine
        return max(left_height, right_height) + 1

    def size(self) -> int:
        if isinstance(self.root.left_node, TerminalNode) or isinstance(self.root.right_node, TerminalNode):
            return 0
        else:
            l = 0
            r = 0
            if self.root.left_node:
                l = self.root.left_node.size() + 1
            if self.root.right_node:
                r = self.root.right_node.size() + 1
            return l + r

    def printTree(self):
        if self.root:
            print(self.root.label)
            if self.root.left_node:
                self.root.left_node.printTree()
            if self.root.right_node:
                self.root.right_node.printTree()

    def parcours_infixe(self, l=None):
        if l is None:
            l = []
        if self.root:
            if self.root.left_node:
                self.root.left_node.parcours_infixe(l)
            if self.root.right_node:
                self.root.right_node.parcours_infixe(l)
            l.append(self.root.label)
        return l

    def terminal(self):
        if self.root:
            if self.root.left_node is None and self.root.right_node is None:
                print(self.root.label)
                self.root.left_node = TerminalNode()
                self.root.right_node = TerminalNode()
            else:
                if self.root.left_node:
                    self.root.left_node.terminal()
                if self.root.right_node:
                    self.root.right_node.terminal()

    def isEqual(self, binary_tree):
        if self.root.label != binary_tree.root.label:
            return False
        else:
            if self.root.left_node:
                v1 = self.root.left_node.isEqual(binary_tree.root.left_node)
            else:
                v1 = True
            if self.root.right_node:
                v2 = self.root.right_node.isEqual(binary_tree.root.right_node)
            else:
                v2 = True

            return v1 == v2

    def isEqual2(self, binary_tree):
        return self.parcours_infixe() == binary_tree.parcours_infixe()

    def isHeap(self):
        if self.root:
            if self.root.left_node:
                if self.root.label > self.root.left_node.root.label:
                    if not self.root.left_node.isHeap():
                        return False
                else:
                    return False
            if self.root.right_node:
                if self.root.label > self.root.right_node.root.label:
                    if not self.root.right_node.isHeap():
                        return False
                else:
                    return False
            return True

class BinaryTreeWithIntegers:
    def __init__(self, nodes: list[int | None] | None = None) -> BinaryTree:
        self.root = None
        if nodes:
            self.root = self._build_tree(nodes, 0)

    def _build_tree(self, nodes, i) -> BinaryTree:
        if i < len(nodes) and nodes[i] is not None:
            return BinaryTree(Node(nodes[i], BinaryTree(self._build_tree(nodes, 2 * i + 1)), BinaryTree(self._build_tree(nodes, 2 * i + 2))))


binary_tree = BinaryTree(Node(2, BinaryTree(Node(4, BinaryTree(Node(0, None, None)), None)),BinaryTree(Node(4, BinaryTree(Node(3, None, None)), BinaryTree(Node(5, None, None))))))
binary_tree2 = BinaryTree(Node(4, BinaryTree(Node(4, BinaryTree(Node(0, None, None)), None)),BinaryTree(Node(4, BinaryTree(Node(3, None, None)), BinaryTree(Node(5, None, None))))))
binary_tree3 = BinaryTree(Node(4, BinaryTree(Node(3, BinaryTree(Node(2, None, None)), BinaryTree(Node(1, None, None)))), BinaryTree(Node(2, None, None))))


# binary_tree.terminal()
# print(binary_tree.isEmpty())
# binary_tree.printTree()
# binary_tree.terminal()
# print(binary_tree.height())
# print(binary_tree.size())

t = [2, 1, 4, 0, None, 3, 5]
v = BinaryTreeWithIntegers(t)
# print(binary_tree.height())
# print(binary_tree.isEqual2(binary_tree2))
# print(binary_tree.parcours_infixe())
print(binary_tree3.isHeap())
