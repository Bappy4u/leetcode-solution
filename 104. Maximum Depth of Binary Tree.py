class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            count = 0
            for i in range(qlen):
                node = q.popleft()
                
                if node:
                    count +=1
                    q.append(node.left)
                    q.append(node.right)
            if count:
                res +=1
            
        return res