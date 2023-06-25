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
        return f'{self.key}'


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newnode = Node(key=value)
        self.__recursive_insert(root=self.root, value=newnode)

    def __recursive_insert(self, root, value):

        if self.root is None:

            self.root = value

        else:
            value.parent = root
            if root.key < value.key:
                if root.right is None:
                    root.right = value
                    root.height = self.__max_child(root)
                    self.__balance(root=root)
                    # root.height = self.__max_child(root)
                else:
                    self.__recursive_insert(root.right, value)

            else:
                if root.left is None:
                    root.left = value
                    root.height = self.__max_child(root)
                    self.__balance(root=root)
                    # root.height = self.__max_child(root)
                else:
                    self.__recursive_insert(root.left, value)

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
        if root.left is None:
            if root.right is not None and root.right.right is not None and root.right.left is None:    # noqa: E501
                return 4
            return 2
        elif root.right is None:
            if root.left is not None and root.left.left is not None and root.left.right is None:    # noqa: E501
                return 3
            return 1

        if (root.left.height > root.right.height) and (root.left.left is not None and root.left.right is not None) and (root.left.left.height > root.left.right.height):    # noqa: E501
            return 1
        elif (root.right.height > root.left.height) and (root.right.right is not None and root.right.left is not None) and (root.right.right.height > root.right.left.height):    # noqa: E501
            return 2
        elif (root.left.height > root.right.height) and (root.left.left is not None and root.left.right is not None) and (root.left.left.height < root.left.right.height):    # noqa: E501
            return 3
        elif (root.right.height > root.left.height) and (root.right.right is not None and root.right.left is not None) and (root.right.right.height < root.right.left.height):    # noqa: E501
            return 4

    def __balance(self, root):
        node = root.parent
        while node is not None:
            if self.__diference(node) > 1:
                c = self.__case(node)

                if c == 1:
                    self.__right_rotation(node)
                elif c == 2:
                    self.__left_rotation(node)
                elif c == 3:
                    self.__left_rotation(node.left)
                    self.__right_rotation(node)
                elif c == 4:
                    self.__right_rotation(node.right)
                    self.__left_rotation(node)

    def __left_rotation(self, node):
        x = node.right
        x.parent = node.parent

        if node.parent is None:
            self.root = x
        elif node is node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x

        node.right = x.left
        if x.left is not None:
            x.left.parent = node

        node.parent = x
        x.left = node

    def __right_rotation(self, node):
        x = node.left
        x.parent = node.parent

        if node.parent is None:
            self.root = x
        elif node is node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x

        node.left = x.right
        if x.right is not None:
            x.right.parent = node

        node.parent = x
        x.right = node


tree = Tree()

tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.print_tree()
