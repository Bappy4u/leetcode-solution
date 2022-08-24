public class Solution {
    public bool IsPowerOfThree(int n) {
        if (n==1){
            return true;
        }
        else if(n!=0 && n%3==0){
            return this.IsPowerOfThree(n/3);
        }
        else{
            return false;
        }
    }
}