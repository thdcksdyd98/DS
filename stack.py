class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        # self.bottom = new_node (since we only care about top)
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.value
