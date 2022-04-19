class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def treeTraverse(root):
            if root:
                treeTraverse(root.left)
                res.append(root.val)
                treeTraverse(root.right)
        
        treeTraverse(root)
        
        return res