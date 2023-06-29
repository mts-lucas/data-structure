import random
import sys
import time

import vetores


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
        self.__recursive_search(root=self.root, key=key)

    def __recursive_search(self, root, key):

        if root is None:
            return False

        elif root.key == key:
            return True

        elif root.key < key:
            return self.__recursive_search(root.right, key)
        else:
            return self.__recursive_search(root.left, key)

    def tree_print_dot_body(self, r, filename):
        with open(filename, 'w') as file:
            file.write("digraph Tree {\n")
            self._tree_print_dot_body_helper(r, file)
            file.write("}\n")

    def _tree_print_dot_body_helper(self, r, file):
        if r is not None:
            self._tree_print_dot_body_helper(r.left, file)
            file.write(f'  "{id(r)}" [label="{{{id(r)}|{r.key}|{{'
                       f'{id(r.left)}|{id(r.right)}}}}}"];\n')
            if r.left:
                file.write(f'  "{id(r)}" -> "{id(r.left)}";\n')
            if r.right:
                file.write(f'  "{id(r)}" -> "{id(r.right)}";\n')
            self._tree_print_dot_body_helper(r.right, file)


if __name__ == "__main__":

    n = int(sys.argv[1])
    # caso medio e melhor caso
    vet = vetores.randv(n)
    # pior caso
    # vet = vetores.sortv(n)
    tree = Tree()
    for i in vet:
        tree.insert(i)

    start = time.time_ns()
    # caso medio
    tree.search(random.randint(1000, 10000))
    # pior caso
    # tree.search(100000000)
    # melhor caso
    # tree.search(vet[0])

    end = time.time_ns()
    final_time = end - start
    print(final_time)
