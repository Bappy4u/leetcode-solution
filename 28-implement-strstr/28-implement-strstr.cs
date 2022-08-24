public class Solution {
    public int StrStr(string haystack, string needle) {
        
        for (int i=0; i<haystack.Length-needle.Length+1; i++){
            string substring = haystack.Substring(i, needle.Length);
            if (substring==needle){
                return i;
            }
        }
        
        return -1;
        
    }
}