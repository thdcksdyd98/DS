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