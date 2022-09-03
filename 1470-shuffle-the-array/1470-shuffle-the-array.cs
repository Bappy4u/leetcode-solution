public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        var len = nums.Length;
        int[] res = new int[len];
        int j=0;
        for(int i=0; i<n; i++){
            res[j]=nums[i];
            j +=2;
        }
        j = 1;
        for(int i = n; i<len; i++ ){
            res[j]=nums[i];
            j +=2;
        }
        return res;
    }
}