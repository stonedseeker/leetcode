import java.util.*;

class SkipApple {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine
        System.out.println(skipApple(str));
    }

    public static String skipApple(String up) {
        if (up.isEmpty()) {
            return "";
        }

        if(up.toLowerCase().startsWith("apple")){
            return skipApple(up.substring(5));
        } else {
           return  up.charAt(0) + skipApple(up.substring(1));
        }
    }
}
