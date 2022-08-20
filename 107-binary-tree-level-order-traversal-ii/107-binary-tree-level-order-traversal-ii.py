# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        
        q.append(root)
        
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.pop(0)
                if node: 
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                
            if level:
                res.append(level)
                
        return res[::-1]
        