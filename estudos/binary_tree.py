class Node:
    def __init__(self, key=None, left=None, right=None) -> None:
        self.key = key
        self.right = right
        self.left = left

    def __str__(self):
        # return f'{self.left} <- {self.key} -> {self.right}'
        return f'{self.key}<'


class Tree:
    def __init__(self) -> None:
        self.root = None
        self.height = None

    def insert(self, value):
        self.root = self._recursive_insert(root=self.root, value=value)

    def _recursive_insert(self, root, value):

        if root is None:
            return Node(key=value)
        else:
            if root.key < value:
                root.right = self._recursive_insert(root=root.right,
                                                    value=value)
            else:
                root.left = self._recursive_insert(root=root.left,
                                                   value=value)

        return root

    def print_tree(self):
        self._recursive_print(self.root)

    def _recursive_print(self, root, level=0):
        if root is not None:
            self._recursive_print(root.right, level=level + 1)
            print('    ' * level + str(root))
            self._recursive_print(root.left, level=level + 1)


tree = Tree()

tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(7)
tree.insert(6)
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.print_tree()
