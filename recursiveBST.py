# contain 
def __r_contains(self,current_node, value):
    if current_node == None:
        return False
    elif value == current_node.value:
        return True
    elif value < current_node.value:
        return self.__r_contains(current_node.left, value)
    elif value > current_node.value:
        return self.__r_contains(current_node.right, value)

def r_contains(self,value):
    return self.__r_contains(self.root, value)

def __r_insert(self, current_node, value):
    if current_node == None:
        return Node(value)
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value)
    return current_node

# searching 'None' value with continuous switching (left and right)
# when the 'None' value was found, creating a new node with input value and adding.
# be aware of 'call stack'

def r_insert(self, value):
    if self.root == None:
        self.root = Node(value)
    self.__r_insert(self.root, value)

def min_value(self, current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value

# delete
# 1. traverse the tree in order to find the node that is going to be deleted
# 2. once the node was founded, delete the node
# 3. what about the sub-tree?? -> connect the sub-tree with a node that was located above the deleted node.
# 4. what if there are two sub-tree (left and right)??
#               -> find the lowest value on the right hand side of sub-tree and copy it to the node that will be deleted
#               -> once the node was copied, delete origianl node (which was located in right hand side of sub-tree)

def __delete_node(self, current_node, value):
    # traverse the tree
    if current_node == None: # empty
        return None
    elif value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    # delete the target
    else:
        # case 1,2,3,4
        # 1. there are no leaf
        # 2. there is a node locating right hand side
        # 3. there is a node locating left hand side
        if current_node.left == None and current_node.right == None:
            return None
        elif current_node.left == None:
            current_node = current_node.right
        elif current_node.right == None:
            current_node = current_node.right
        else:
            # 4. case where there are sub-trees in both right and left hand side
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node