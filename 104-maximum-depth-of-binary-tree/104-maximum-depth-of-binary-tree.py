# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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