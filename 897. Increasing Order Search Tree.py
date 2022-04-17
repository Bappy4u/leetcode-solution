class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        
        def readBST(nroot):
            if not nroot:
                return
            if nroot.left:
                readBST(nroot.left)
            res.append(nroot.val)
            if root.right:
                readBST(nroot.right)
            
            
        
        readBST(root)
        resNode = TreeNode(0)
        temp = resNode
        for i in res:
            temp.right = TreeNode(i)
            temp = temp.right
          
            
        return resNode.right
            