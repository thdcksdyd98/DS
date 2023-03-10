# Breadth First Search
# starting from root node, traversing every node from left to right

def BFS(self):
    current_node = self.root
    queue = []
    results = []
    queue.append(current_node)

    while len(queue) > 0: # if we did not append the root node, the while loop will be terminated
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    
    return results

# Depth First Search
# 1. Pre-Order -> traverse left; if there were no leaf move to previous node and traverse right 

def dfs_pre_order(self):
    results = []

    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
    
    traverse(self.root)
    return results

# 2. Post-Order -> traverse left hand side first; find all leaf nodes and return them. then, move to previous level of nodes.

def dfs_post_order(self):
    results = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)
    
    traverse(self.root)
    return results

# 3. In-Order -> start from left hand side of sub-tress, traverse entire tree
# can traverse entire node with order.
def dfs_in_order(self):
    results = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)  

    traverse(self.root)
    return results
