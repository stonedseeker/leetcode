import java.util.HashMap;
import java.util.*;

class Parenthesis {
    public static void main(String[] args) {
        String s = "()((";
        System.out.println(removeParenthesis(s));
    }

     public static String removeParenthesis(String s) {
        int countOpen = 0;
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                countOpen++;
                res.append(c);
            } else if (c == ')' && countOpen > 0) {
                countOpen--;
                res.append(c);
            }
        }

        return res.toString();
    }

    public static String removeParenthesis2(String s) {
        // HashMap<Character, Integer> map = new HashMap<>();
        //
        // for (int i = 0; i < s.length(); i++) {
        //     char c = s.charAt(i);
        //     map.put(c, map.getOrDefault(c, 0) + 1);
        // }
        //
        // if (map.get('(') == map.get(')')) return s;
        // 
        StringBuilder res = new StringBuilder();

        int count_1 = 0;
        int count_2 = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' && count_1 < count_2+1){
                res.append(c);
                count_1++;
            } if (c == ')' && count_2 < count_1) {
                res.append(c);
                count_2++;
            }
        }
    

        // System.out.println(map);
        return res.toString();
    }
}
