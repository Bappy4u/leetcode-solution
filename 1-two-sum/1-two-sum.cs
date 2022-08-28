public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary < int, int > map = new Dictionary < int, int > ();
        
        var res = new int[2];
        for (int i=0; i<nums.Length; i++ ){
            var diff = target - nums[i];
            
            if (map.ContainsKey(diff)){
                int[] res1 = {map[diff],i};
                return res1;
            }
            else{
                map[nums[i]]=i;
            }
        }
        return res;
    }
}