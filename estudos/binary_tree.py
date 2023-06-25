class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newnode = Node(key=value)
        self.__recursive_insert(root=self.root, value=newnode)

    def __recursive_insert(self, root, value):
        if self.root is None:
            self.root = value
        else:
            if root.key < value.key:
                if root.right is None:
                    root.right = value
                else:
                    self.__recursive_insert(root=root.right, value=value)
            else:
                if root.left is None:
                    root.left = value
                else:
                    self.__recursive_insert(root=root.left, value=value)

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
