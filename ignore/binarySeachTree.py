from logging import root
from multiprocessing.sharedctypes import Value
from xmlrpc.client import Boolean


class Node():
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None 
    def __repr__(self) -> str:
        return f"value: {self.value}"

class Tree():
    def __init__(self) -> None:
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if current.value>value:
                    if not current.left:
                        current.left = Node(value)
                        current = None
                    else:
                        current = current.left
                else:
                    if current.value<value:
                        if not current.right:
                            current.right = Node(value)
                            current = None
                        else:
                            current = current.right
    
    def find(self, value) -> bool:
        current = self.root

        while current:
            if current.value == value:
                return True
            elif current.value<value:
                current = current.right
            else:
                current = current.left
        return False




btree = Tree()

btree.insert(5)
btree.insert(7)
btree.insert(6)
btree.insert(8)
btree.insert(9)
btree.insert(4)
btree.insert(3)
btree.insert(2)
btree.insert(1)



print(btree.find(7), btree.find(10))
                        


    


