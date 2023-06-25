class Node:
    def __init__(self, key=None,
                 left=None,
                 right=None,
                 parent=None,
                 height=1) -> None:

        self.key = key
        self.right = right
        self.left = left
        self.parent = parent
        self.height = height

    def __str__(self):
        return self.key


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        self.root = self.__recursive_insert(root=self.root, value=value)

    def __recursive_insert(self, root, value, parent=None):

        if root is None:

            return Node(key=value, parent=parent)

        else:

            if root.key < value:

                root.right = self.__recursive_insert(root=root.right,
                                                     value=value,
                                                     parent=root)
                root.height = self.max_child(root)

            else:
                root.left = self.__recursive_insert(root=root.left,
                                                    value=value,
                                                    parent=root)
                root.height = self.max_child(root)

        return root

    def print_tree(self):
        self.__recursive_print(self.root)

    def __recursive_print(self, root):
        if root is not None:
            self.__recursive_print(root.left)
            print(root.key)
            self.__recursive_print(root.right)

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

    def search(self, key):
        print(self.__recursive_search(root=self.root, key=key))

    def __recursive_search(self, root, key):

        if root is None:
            return False

        elif root.key == key:
            return True

        elif root.key < key:
            return self.__recursive_search(root.right, key)
        else:
            return self.__recursive_search(root.left, key)

    def __max_child(self, node: Node):
        lcompair = 0
        rcompair = 0

        if node.left is not None:
            lcompair = node.left.height
        if node.right is not None:
            rcompair = node.right.height

        if lcompair >= rcompair:
            return lcompair + 1

        return rcompair + 1

    def __diference(self, node):
        lcompair = 0
        rcompair = 0

        if node.left is not None:
            lcompair = node.left.height
        if node.right is not None:
            rcompair = node.right.height

        if lcompair >= rcompair:
            return lcompair - rcompair

        return rcompair - lcompair

    def __case(self, root: Node):
        if (root.left.heigth > root.right.heigth) and (root.left.left.heigth > root.left.right.heigth):  # noqa: E501
            return 1
        elif (root.right.heigth > root.left.heigth) and (root.right.right.heigth > root.right.left.heigth):  # noqa: E501
            return 2
        elif (root.left.heigth > root.right.heigth) and (root.left.left.heigth < root.left.right.heigth):  # noqa: E501
            return 3
        elif (root.right.heigth > root.left.heigth) and (root.right.right.heigth < root.right.left.heigth):  # noqa: E501
            return 4

    def __balance(self, root):
        if self.__diference(root) > 1:
            c = self.__case(root)

            if c == 1:
                self.__right_rotation(root)
            elif c == 2:
                self.__left_rotation(root)
            elif c == 3:
                self.__left_rotation(root.left)
                self.__right_rotation(root)
            elif c == 4:
                self.__right_rotation(root.right)
                self.__left_rotation(root)

    def __left_rotation(self, node):
        pass

    def __right_rotation(self, node):
        pass


tree = Tree()

tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.search(7)
tree.print_tree()
