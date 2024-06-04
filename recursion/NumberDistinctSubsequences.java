import java.util.ArrayList;
import java.util.List;


class NumberDistinctSubsequences {
    public static void main(String[] args) {
        System.out.println(distinctSubsequences("vaibhav"));
    }

    
    public static int distinctSubsequences(String S) {
        List<Character> list = new ArrayList<>();
        List<String> ds = new ArrayList<>();
        
        return dfs(S, list, ds, 0);
    }
    
    public static int dfs(String S, List<Character> list, List<String> ds, int index) {
        if (index == S.length()) {
            String res = "";
            for (Character c : list) {
                res += c;
            }
            if (!ds.contains(res)) {
                ds.add(res);
                return 1;
            } else {
                return 0;
            }
        }
        
        list.add(S.charAt(index));
        int left = dfs(S, list, ds, index+1);
        
        list.remove(list.size() - 1);
        int right = dfs(S, list, ds, index+1);
        
        return left + right;
        
    }
}

