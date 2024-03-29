# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0
            elif not root.left and root.right:
                return 1+ depth(root.right)
            elif not root.right and root.left:
                return 1+(depth(root.left))
            
            else:
                left = depth(root.left)
                right = depth(root.right)


                return 1+min(left,right)
        
        return depth(root)
    