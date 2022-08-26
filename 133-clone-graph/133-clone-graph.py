"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        if not node:
                return
        def dfs(node):
            
            if oldToNew.get(node):
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
                
            return copy
        
        
        return dfs(node)
        