# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []   
        def bst(val):
            if val:
                bst(val.left)
                res.append(val.val)
                bst(val.right)
                
        
        bst(root)
        return res
            
        