class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp)
            tmp = tmp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        else:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            tmp.prev = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
        return tmp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            target = self.head
            self.head = self.head.next
            target.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return target

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            '''
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next

            # still works but not efficient
            '''
            if index < self.length / 2:
                tmp = self.head
                for _ in range(index):
                    tmp = tmp.next
            else:
                tmp = self.tail
                for _ in range(self.length - 1, index, -1):
                    tmp = tmp.prev 
        return tmp

    def set(self, index, value):
        tmp = self.get(index)
        if tmp != None:
            tmp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            start = self.get(self,index -1)
            end = start.next
            new_node.prev = start
            new_node.next = end
            start.next = new_node
            end.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            '''
            tmp = self.get(index)
            start = tmp.prev
            end = tmp.next
            start.next = end
            end.prev = start
            tmp.prev = None
            tmp.next = None
            '''
            # more concise
            tmp = self.get(index)
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp.next = None
            tmp.prev = None
        
        self.length -= 1    
        return tmp


        



