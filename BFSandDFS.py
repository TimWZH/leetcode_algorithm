# BFS
# 1. Simple queue
# 2. Dequeue (Double ended queue)
# 3. DummyNode

# 1. Simple queue
import collections
def levelOrder(self, root):
    if root is None:
        return []
    queue = collections.deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
               queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result 

# 2. Dequeue
def levelOrder(self, root):
    if not root:
        return []
    queue = [root]
    results = []
    while queue:
        next_queue = []
        results.append([node.val for node in queue])
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return results

# 3. dummy node
def levelOrder(self, root):
    if root is None:
        return []
    queue = collections.deque([root, None])
    results, level = [], []
    while queue:
        node = queue.popleft()
        if node is None:
            results.append(level)
            level = []
            if queue:
                queue.append(None)
            continue
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return results

# 1. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator:
    def __init__(self,root):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0
    
    def Next(self):
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node

# solution 2
class BSTIterator2:
    
    def __init__(self, root):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left
    
    def hasNext(self) :
        return len(self.stack) > 0

    def next(self):
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val



################################################## 
# When to use BFS:
# 1. Connected Component
# 2. Level Order Traversal
# 3. 