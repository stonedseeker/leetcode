class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.children.extend([node2, node4, node3, node5])
node2.children.extend([node4, node1])
node3.children.extend([node1])
node4.children.extend([node2, node1])
node5.children.append(node1)



visited = []

def dfs(root: Node, visited):
    if root in visited:
        return 
    print(root.value)
    visited.add(root)
    for c in root.children:
        dfs(c, visited)
    
visited = set()

dfs(node2, visited)
