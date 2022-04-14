class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        
        if (root==null){
            return root;
        }
        if (root.val==val){
           
            return root;
        }
        if (root.val<val){
            return this.searchBST(root.right, val);
        }
        else{
            return this.searchBST(root.left, val);
        }
           
    }
   
}