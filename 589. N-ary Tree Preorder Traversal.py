class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        def preOrder(child):
            if not child:
                return
            res.append(child.val)
            for child in child.children:
                preOrder(child)

            
        preOrder(root)
        
        return res
        