public class Solution {
    public string DecodeString(string s) {
        Stack<string> characters = new Stack<string>();
        Stack digits = new Stack();
        var i = 0;
        while (i<s.Length){
            if (Char.IsDigit(s[i])){
                var d = 0;
                while(Char.IsDigit(s[i])){
                    
                    d = (d*10) + int.Parse(s[i].ToString());
                    
                    i++;
                }
                
                digits.Push(d);
            }
            
            else if (s[i].Equals(']')){
                
                var temp = "";
                
                while (true){
                    var x = characters.Pop();
                    
                    if (x.Equals("[")) break;
                    
                    temp = x + temp;
                }
                
                string str = string.Concat(Enumerable.Repeat(temp, (int)digits.Pop()));
                characters.Push(str);
                i++;
            }
            
            else{
                characters.Push(s[i].ToString());
                i++;
            }
        }
        
        string res = "";
        
        foreach(var st in characters){
            
            res = st + res;
        }
        
        return res;
    }
}