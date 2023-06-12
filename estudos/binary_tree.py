class Node:
    def __init__(self, key=None, left=None, right=None) -> None:
        self.key = key
        self.right = right
        self.left = left

    def __repr__(self):
        return f'{self.left} <- {self.key} -> {self.right}'
