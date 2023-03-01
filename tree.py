class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        else:
            tmp = self.root
            while (True):
                if new_node.value == tmp.value:
                    return False
                elif new_node.value < tmp.value: # left side
                    

                elif new_node.value > tmp.value: 



