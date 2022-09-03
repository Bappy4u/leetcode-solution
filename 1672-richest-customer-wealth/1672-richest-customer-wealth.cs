public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int res = 0;
        foreach(var ac in accounts){
            
            
            res = Math.Max(res, ac.Sum());
        }
        
        return res;
    }
}