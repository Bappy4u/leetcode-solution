public class Solution {
    public bool IsValid(string s) {
        Stack<char> st = new Stack<char>();
        var parenthesis = new Dictionary<char, char>(){
            {'}','{'},
            {']','['},
            {')', '('}
        };
        
        for(int i=0; i<s.Length; i++){
            if (st.Count()>0 && parenthesis.ContainsKey(s[i]) && st.Peek()==parenthesis[s[i]]){
                    st.Pop();
                }
            else{
                st.Push(s[i]);
            }
                
            }
        
        return st.Count()==0;
        
    }
}