class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrder(root):
            if root:
                res.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
                                
        preOrder(root)
        
        return res
        