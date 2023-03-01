class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def printqueue(self):
        tmp = self.first
        while tmp is not None:
            print(tmp)
            tmp = tmp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            return None
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
