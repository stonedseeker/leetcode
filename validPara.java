import java.util.Stack;

class validPara {
    public static void main(String[] args) {
        String strs = "()[]{}";
        System.out.println(isValid(strs));
    }

    
    public static boolean isValid(String s) {
        Stack stk = new Stack();
        stk.push("hello");
        stk.push("zerlin");
        
        // for (int i = 0; i < s.length(); i++) {
        //     if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[' ) {
        //         stk.push(s.charAt(i));
        //     } if (s.charAt(i) == ')' && stk.peek() == '(' || s.charAt(i) == ']' && stk.peek() == '[' || s.charAt(i) == '}' && stk.peek() == '{'){
        //         continue;
        //     } else return false;
        // }
        // 
        //
        System.out.println(stk.peek());
        System.out.println(stk.peek().equals("zerlin"));
        return true;
    }

}
