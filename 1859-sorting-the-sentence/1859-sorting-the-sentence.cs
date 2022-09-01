public class Solution {
    public string SortSentence(string s) {
        List<string> list = new List<string>();
        
        list = s.Split(" ").ToList();
        string[] ar = new string[list.Count];
        
        foreach(var word in list){
            int i = int.Parse(word[word.Length-1].ToString());
            
            ar[i-1] = word.Substring(0, word.Length-1);
        }
        
        return String.Join(" ", ar);
    }
}