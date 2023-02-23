class Node:
    def __init__(self, value):
        # generate node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def printlist(self):
        tmp = self.head
        if tmp.next is not None:
            print(tmp.value)
            tmp = tmp.next

    def append(self, value):
        new_node = Node(value)
        # if the node were not existed
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1 
        return True
        
    def pop(self):
        # before decrement; checking length of the list
        if self.length == 0:
            return None
        else:
            tmp = self.head
            pre = self.head
            while tmp.next is not None:
                # 'pre' should be first
                pre = tmp
                tmp = tmp.next
            # when tmp.next is None; the pre points the node
            # that will become tail after pop
            # also, it breaks the last node from the list
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            # after decrement
            if self.length == 0:
                self.head = None
                self.tail = None
        # return the value that we just removed
        # tmp: address, tmp.value: actual value
        return tmp

    def popfirst(self):
        if self.length == 0:
            return None
        else:
            target = self.head
            self.head = self.head.next # if there were only one node, node.next will be None
            target.next = None
            self.length -= 1
            if self.length == 0:
                # self.head = None ;already equals to None if there were only one node. 
                self.tail = None
        return target

    def get(self, index):
        # when the index is out of range
        if index < 0 or index >= self.length: 
            return None
        else: 
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
            return tmp

    def set_value_v1(self, index, value):
        if index < 0 or index >= self.length:
            return None
        elif index:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
            tmp.value = value
            return True
        else:
            return False
    
    def set_value_v2(self, index, value):
        tmp = self.get(index)
        '''
        if index < 0 or index >= self.length:
                    return None
                else:
                    tmp = self.head
                    for _ in range(index):
                        tmp = tmp.next        
        '''
        if tmp: # if tmp is not None
            tmp.value = value
            return True
        return False

    def insert(self, index, value):
        # can insert the value into the last index (self.length)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            tmp = self.get(index - 1)
            new_node.next = tmp.next
            tmp.next = new_node
            self.length += 1
            return True
 

#  adding: return True or False
#  removing: return value or None (if removing were successufull, returning the removed value)

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            tmp = self.get(index - 1)
            # target = self.get(index) O(n)
            target = tmp.next # O(1)
            tmp.next = target.next
            target.next = None
            self.length -= 1
            return target

    def reverse(self):
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        after = tmp.next
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before
            # after the code above, there will be an gap bewteen tmp and after
            # so, have to fill the gap
            before = tmp
            tmp = after

# interview questions (1)
# Find Middle Node: Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute. 
# hint: creating two variables: fast and slow
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def find_middle_node(self): 
        '''
        Finds the middle node of the linked list using the 
        "slow and fast pointers" technique.
 
        Returns:
        - If the length of the linked list is even, returns the second middle node.
        - If the length of the linked list is odd, returns the middle node.
 
        Time complexity: O(n)
        Space complexity: O(1)      
        '''
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

# interview questions (2)
# Has Loop: Write a method to determine if the Linked List contains a loop.
# hint: creating two variables: fast and slow

    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# interview questions (3)
# Remove Duplicates: Remove all duplicates from the Linked List.
# hint: 1. using set (O(n)) 2. using loop that iterates the LinkedList (O(n^2))

# using set
    def remove_duplicates(self):
        ans = set()
        previous = None
        current = self.head
        while current:
            # if the current is in the set
            if current.value in ans:
                # skipping the current node; 
                previous.next = current.next
                # after skipping, reduce the length
                self.length -= 1
            # if the current is not in the set
            else:
                # adding the current node into the set
                ans.add(current.value)
                # move forward (previous를 current로 바꾸어서 한 노드씩 앞당김.)
                previous = current
            # checking the next node
            current = current.next 

# using loop
    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next


# interview questions (4) 
# Find Kth node from the end

    def find_kth_from_end(head, k):
        '''
        similar to sliding window
        '''
        start = end = head
        for _ in range(k):
            if end is None:
                return None
            end = end.next
        while end: 
            start = start.next
            end = end.next
        return start



    "test"
