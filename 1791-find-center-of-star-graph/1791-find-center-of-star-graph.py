class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = []
        for node,node1 in edges:
            nodes.append(node)
            nodes.append(node1)
           
        for node in nodes:
            j = len(edges)
            for k in edges:
                if node not in k:
                    break
                j -=1
            if j==0:
                return node
            