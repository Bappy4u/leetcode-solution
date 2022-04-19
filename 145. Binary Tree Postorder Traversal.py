class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def treeTraverse(root):
            if root:
                treeTraverse(root.left)
                treeTraverse(root.right)
                res.append(root.val)

        treeTraverse(root)
        
        return res
        