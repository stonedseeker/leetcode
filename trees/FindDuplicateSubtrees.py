from typing import DefaultDict, List, Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
            self.val = val
            self.left = left
            self.rigth = right

class Solution:

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = DefaultDict(list)

        def dfs (node):
            if not node:
                return "null"
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
            
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        res = []
        dfs(root)
        return res
            
