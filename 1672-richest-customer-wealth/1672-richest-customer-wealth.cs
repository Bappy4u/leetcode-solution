public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int res = 0;
        foreach(var ac in accounts){
            var sum = 0;
            foreach(var e in ac){
                sum +=e;
            }
            
            res = Math.Max(res, sum);
        }
        
        return res;
    }
}