class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return isMirror(p.left, q.right) and isMirror(p.right, q.left)
        
        
        return isMirror(root.left, root.right)
        