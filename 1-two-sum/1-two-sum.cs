public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary < int, int > map = new Dictionary < int, int > ();
        
        var res = new int[2];
        for (int i=0; i<nums.Length; i++ ){
            var diff = target - nums[i];
            
            if (map.ContainsKey(diff)){
                res[0]=map[diff];
                res[1]=i;
                return res;
            }
            else{
                map[nums[i]]=i;
            }
        }
        return res;
    }
}