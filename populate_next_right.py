from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Tree:
    def buildTree(self, nums):
        if not nums:
            return None
        
        root = TreeNode(nums[0])
        nodes = [root]
        for i in range(1, len(nums), 2):
            parent = nodes.pop(0)
            if nums[i] is not None:
                left_child = TreeNode(nums[i])
                parent.left = left_child
                nodes.append(left_child)
            if i + 1 < len(nums) and nums[i + 1] is not None:
                right_child = TreeNode(nums[i + 1])
                parent.right = right_child
                nodes.append(right_child)
        
        return root




# Now `balanced_tree` is a perfectly balanced binary search tree.
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                if node.left:
                    node.left.next = node.right
                if node.right:
                    node.right.next = None
                q.append(node.left)
                q.append(node.right)

        return root
            
        

root = [1, 2, 3, 4, 5, 6, 7]
tree = Tree()
balanced_tree = tree.buildTree(root)
print(Solution().connect(balanced_tree))

