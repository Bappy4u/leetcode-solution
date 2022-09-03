public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int[] res = new int[nums.Length*2];
        int n=nums.Length;
        for(int i=0; i<res.Length; i++){
            if(i<nums.Length){
                res[i]=nums[i];
            }
            else{
                res[i]=nums[i-n];
            }
        }
        return res;
    }
}