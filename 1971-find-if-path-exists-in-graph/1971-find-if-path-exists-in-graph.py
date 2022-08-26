class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if destination==source:
            return True
        
        nodes = {node:[] for node in range(n)}

        for frm,to in edges:
            nodes[frm].append(to)
            nodes[to].append(frm)
        
        visited = set()
        q = deque()
        q.append(nodes[source])
        
        visited.add(source)
        while q:
            x = q.popleft()
            print(x)
            if destination in x:
                return True
            for d in x:
                if d not in visited:
                    q.append(nodes[d])
                    visited.add(d)
                    
        return False
                    
        