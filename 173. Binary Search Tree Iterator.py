class BSTIterator:
    def postorder(self,root):
        if root:
            self.postorder(root.right)
            self.bst.append(root.val)
            self.postorder(root.left)
        
    def __init__(self, root: Optional[TreeNode]):
        self.bst=[]
        self.postorder(root) 

    def next(self) -> int:
        if self.bst:
            return self.bst.pop()

    def hasNext(self) -> bool:
        if self.bst:
            return True