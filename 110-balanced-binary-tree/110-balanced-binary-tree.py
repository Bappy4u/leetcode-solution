# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def maxheight(root):
            if root:
                left = root.left
                right = root.right
                return 1+max(maxheight(left), maxheight(right))
            
            return 0
        
        
        def bst(root):
            if root:
                leftdiff = abs(maxheight(root.left) - maxheight(root.right))
                if leftdiff>1:
                    print(leftdiff)
                    return False
                return bst(root.left) and bst(root.right)
                
            return True
            
        return bst(root)
        