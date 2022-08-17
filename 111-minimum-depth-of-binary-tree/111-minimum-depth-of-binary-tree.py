# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        q = []
        
        q.append(root)
        
        while q:
            level = 0
            qlen = len(q)
            
            for i in range(qlen):
                node = q.pop(0)
                
                if node and not node.left and not node.right:
                    return depth+1
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level = 1
                    
            if level:
                depth +=1

        return depth