import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class PalindromePartitioning {
    public static void main(String[] args) {
        String s = "aab";
        System.out.println(partition(s));
    }

    public static List<List<String>> partition(String s) {
        
        List<List<String>> res = new ArrayList<>();
        List<String> list = new ArrayList<>();
        dfs(0, s, res, list);
        return res;
    } 

    public static void dfs(int index, String s, List<List<String>> res, List<String> list) {
        if (index == s.length()) {
            for (String str : list) {
                if (!isPalindrome(str) && str != "") 
                    break;
            }
            res.add(new ArrayList<>(list));
            return;
        }

        list.add(s.substring(0, index));
        dfs(index + 1, s, res, list);
        list.remove(list.size() - 1);
        dfs(index + 1, s, res, list);

    }

    public static boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l <= r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }

        return true;
        
    }
}
