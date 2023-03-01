# A B C D가 리스트의 형태로 있다고 가정. 
# 리스트의 맨 마지막 부분에 pop/push는 O(1)
# 리스트의 맨 첫번째 부분에 pop/push는 O(n) -> 인덱스가 모두 재 정렬 되어야 하기 때문
# 따라서 리스트일 경우에는
# D
# C
# B
# A

# A B C D가 LL의 형태로 있다고 가정
# LL의 맨 마지막 부분에서 pop은 O(n), push는 O(1)
# LL의 맨 첫번째 부분에서 pop/push는 O(1)
# 따라서 LL일 경우에는 리스트일 경우와 반대가 되어야 한다
# A
# B
# C
# D
# 그래서 self.top은 A가 되어야 함.

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node # self.head가 top이 됨. 
        # self.bottom = new_node (since we only care about top)
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.value

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            target = self.top
            self.head = self.head.next
            target.next = None
            self.height -= 1
            if self.height == 0:
                self.top == None
        return target
            
