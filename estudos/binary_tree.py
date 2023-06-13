class Node:
    def __init__(self, key=None, left=None, right=None) -> None:
        self.key = key
        self.right = right
        self.left = left

    def __str__(self):
        return f'{self.key}'


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
        self.__recursive_print(self.root)

    def __recursive_print(self, root, level=0):
        if root is not None:
            self._recursive_print(root.right, level=level + 1)
            print('    ' * level + str(root))
            self._recursive_print(root.left, level=level + 1)

    def ascending_order(self):
        self.__ascending_order(self.root)

    def __ascending_order(self, root):
        if root is not None:
            self.__ascending_order(root.left)
            print(root.key)
            self.__ascending_order(root.right)

    def decreasing_order(self):
        self.__decreasing_order(self.root)

    def __decreasing_order(self, root):
        if root is not None:
            self.__decreasing_order(root.right)
            print(root.key)
            self.__decreasing_order(root.left)


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
# tree.print_tree()
# tree.ascending_order()
tree.decreasing_order()
