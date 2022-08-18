class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        q = []
        
        q.append(root)
        
        while q:
            level = []
            
            qlen = len(q)
            
            for i in range(qlen):
                node = q.pop(0)
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                    
            if level:
                depth +=1
        return depth