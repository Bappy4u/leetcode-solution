import java.lang.reflect.Array;
class Solution {
     public static int[] addX(int arr[], int x) {
        int i, n = arr.length;
  
        int newarr[] = new int[n + 1];
  
        for (i = 0; i < n; i++)
            newarr[i] = arr[i];
  
        newarr[n] = x;
  
        return newarr;
    }
    
    public int lastStoneWeight(int[] stones) {
        int x, y;
        Arrays.sort(stones);
        
        while (stones.length>1){
            x = (int)Array.get(stones, stones.length-1);
            y = (int)Array.get(stones, stones.length-2);
            stones = Arrays.copyOf(stones, stones.length-2);
            if (x-y>0){
                stones = addX(stones, x-y);
                Arrays.sort(stones);
                
            }
        }
        
        if (stones.length>0)
            return (int)Array.get(stones, 0);
        else{
            return 0;
        }
        
        
    }
}