public class Solution {
    public int MostWordsFound(string[] sentences) {
        string[] temp;
        int res = 0;
        for(int i=0; i<sentences.Length; i++){
            temp = sentences[i].Split(" ");
            res = Math.Max(temp.Length, res);
            
            
        }
        
        return res;
        
    }
}