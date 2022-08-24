public class Solution {
    public bool IsValid(string s) {
        Stack<char> st = new Stack<char>();
        var parenthesis = new Dictionary<char, char>(){
            {'}','{'},
            {']','['},
            {')', '('}
        };
        
        for(int i=0; i<s.Length; i++){
            
            if (!parenthesis.ContainsKey(s[i])){
                st.Push(s[i]);
            }
            else{
                if (st.Count()>0 && st.Peek()!=parenthesis[s[i]]){
                    return false;
                }
                else{
                    if (st.Count()>0){
                        st.Pop();
                    }
                    else{
                        st.Push(s[i]);
                    }
                    
                }
            }
        }
        
        return st.Count()==0;
        
    }
}