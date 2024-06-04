import java.util.Arrays;

class Susequences {
    public static void main(String[] args) {
        skiped("", "baccaad");
        System.out.println("Strin" + 'g');
        System.out.println(skip("aaabbbbbadsad"));
        System.out.println(skipApple("thisappleisverytastyandbetterthanotherapples"));
    }

     public static String skipApple(String up) {
        if (up.isEmpty()){
            return "";
        }

        if (up.startsWith("apple")){
            return skipApple(up.substring(5));
        } else {
            return up.charAt(0) + skipApple(up.substring(1));
        }
    }


    public static String skip(String up) {
        if (up.isEmpty()){
            return "";
        }

        if (up.charAt(0) == 'a'){
            return skip(up.substring(1));
        } else {
            return up.charAt(0) + skip(up.substring(1));
        }
    }



    public static void skiped(String p, String up) {
        if (up.isEmpty()){
            System.out.println(p);
            return;
        }

        if (up.charAt(0) == 'a'){
            skiped(p, up.substring(1));
        } else {
            skiped(p + up.charAt(0), up.substring(1));
        }
    }


    public static void subSec(int[] nums, int idx) {
        if (idx >= nums.length) {
            System.out.println(Arrays.toString(nums));
            return;
        }

        // subSec(nums.substring(0,))
    }

    }
