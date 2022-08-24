public class Solution {
    public bool IsPowerOfFour(int n) {
        if(n==1){
            return true;
        }
        else if(n!=0 && n%4==0){
            return this.IsPowerOfFour(n/4);
        }
        else{
            return false;
        }
        
    }
}