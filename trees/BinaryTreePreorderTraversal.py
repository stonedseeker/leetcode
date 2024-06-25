# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
   

        def recursive(root, stack = []):
            if root is None:
                return []
            
            stack.append(root.val)
            recursive(root.left, stack)
            recursive(root.right, stack)
            return stack

        return recursive(root, stack = [])

root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))

print(Solution().preorderTraversal(root))
