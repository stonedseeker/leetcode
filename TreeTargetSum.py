#class TreeNode:
#   def __init__(self, val = 0, next = None):
#       self.val = val
#       self.next = None


from collections import deque

class TreeNode:
    def __init__(self, data,  left, right):
        self.data = data
        self.left = left
        self.right = right



leaf6 = TreeNode(6, None, None)
leaf2 = TreeNode(2, None, None)
node5 = TreeNode(5, None, leaf6)

leaf1  = TreeNode(1, None, None)
node4 =  TreeNode(4, leaf1,leaf2)

leaf11 =  TreeNode(1, None, None)

node1 =  TreeNode(1, leaf11, None)
node2 = TreeNode (2, None, None)
three =  TreeNode(3, node2, node1)

minusOne =  TreeNode(-1, node4, node5)

root =  TreeNode(1, three, minusOne)

q = deque()

res = []

q.append(root)

while q:
    level = []
    qLen = len(q)

    for i in range(qLen):
        node = q.popleft()
        if node:
            level.append(node)
            q.append(node.left)
            q.append(node.right)

    res.append(level)

res.pop()

for level in res:
    print("level = ", end = "")
    for node in level:
        print(node.data,  " " , end = "")
    print()



def sumK(root,k):
        
        def dfs(node, count, ans):
            if not node:
                return ans
            count += node.data
            
            if count == k:
                return dfs(node.left, count, ans+1) + dfs(node.right, count, ans+1)
            else: return dfs(node.left, count, ans) + dfs(node.right, count, ans)
    
        return dfs(root, 0,0)
print(sumK(root, 5))
        







