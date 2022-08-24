public class Solution {
    public int StrStr(string haystack, string needle) {
        
        for (int i=0; i<haystack.Length-needle.Length+1; i++){
            int temp = needle.Length;
            int k = 0;
            Console.WriteLine(i);
            for (int j=i; j<i+needle.Length; j++){
                Console.WriteLine(j);
                if (haystack[j]==needle[k]){
                    temp--;
                   
                }
                else{
                    break;
                }
                k++;
            }
            if (temp==0){
                return i;
            }
        }
        
        return -1;
        
    }
}