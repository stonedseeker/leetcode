from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None

        res = []
        while root:
            res.append(root.val)
            root = root.right
        
        return res


#root = TreeNode(1)
#node2 = root.left = TreeNode(2)
#node3 = root.right = TreeNode(3)
#node2.right = TreeNode(5)
#node3.right = TreeNode(4)

root = TreeNode(1)
root.right = TreeNode(2)

print(Solution().rightSideView(root))

