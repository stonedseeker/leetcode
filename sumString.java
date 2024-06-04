import java.util.*;
class sumString{

    public static String sum(String s1, String s2) {
        StringBuilder sb = new StringBuilder();
        
        int i = s1.length() - 1, j = s2.length() - 1, sum = 0, rem = 0, carry = 0;
        
        while(i >= 0 || j >= 0 || carry == 1) {
            sum = (i >= 0 ? s1.charAt(i) - '0' : 0) + (j >= 0 ? s2.charAt(j) - '0' : 0) + carry;
            i--; j--;
            carry = sum / 10;
            rem = sum % 10;
            sb.append(rem);
            System.out.println(sb);
        }

        System.out.println(sb);
        
        sb.reverse();

        System.out.println("sb " + sb);

        return sb.toString();
    }

    public static void main(String[] args) {
        String str1 = "ab";
        String str2 = "ab";

        String s = sumString.sum(str1, str2);
        System.out.println(s);

        // System.out.println(sum(str1, str2));
    }
}
