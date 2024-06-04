#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from collections import deque
from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            print(qLen)
            print(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res



class Tree:
    node5 = TreeNode(7)
    node4 = TreeNode(15)
    node3 = TreeNode(20, node4, node5)
    node2 = TreeNode(9)
    node1 = TreeNode(3, node2, node3)

    print(Solution().levelOrder(node1))
