# Definition for a binary tree node.


import builtins


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      
        if not preorder:
            return None 
        

        root, index = TreeNode(preorder[0]), 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
        #index = inorder.index(root.val)


        root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index+1 :], inorder[index + 1 : ])


