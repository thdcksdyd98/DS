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
                if new_node.value == tmp.value: # identical value
                    return False
                
                elif new_node.value < tmp.value: # left side; if new value is less than current node's(tmp) value
                    if tmp.left is None: # add new node if there were no other sub trees in left side of current node.
                        tmp.left = new_node
                        return True
                    
                    else:
                        tmp = tmp.left # if there were other sub trees, left side of current node is the new current node
                        # and will be compared with new node again through while loop.
                
                elif new_node.value > tmp.value: # right side
                    if tmp.right is None:
                        tmp.right = new_node
                        return True
                    
                    else:
                        tmp = tmp.right
                        
    # Since it is a 'searching' process, checking other subtrees are not required. 
    # Thus, if the value is less or greater than the current node, the current node should be changed to left or right.
    
    def contains(self, value):
        if self.root == None:
            return False
        else:
            tmp = self.root
            while tmp is not None:
                if value == tmp.value:
                    return True
                
                elif value < tmp.value:
                    tmp = tmp.left

                elif value > tmp.value:
                    tmp = tmp.right

                else:
                    return False


