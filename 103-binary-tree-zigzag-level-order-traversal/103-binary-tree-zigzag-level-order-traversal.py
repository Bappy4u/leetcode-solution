# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = []
        res = []
        q.append(root)
        
        z = 0
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):         
                node = q.pop(0)

                if node:
                    level.append(node.val)
  
                    q.append(node.left)
                    q.append(node.right)

            if level:
                if z%2==1:
                    level = level[::-1]
                
                res.append(level)
            z +=1       
        return res
        