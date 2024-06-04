// Given two strings s and t of lengths ma and n respectively, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

class MInimumWindowSubstring {
    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s, t));
    }
// abc acb bac bca cab cba 
    public static String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }

        int[] tCount = new int[128];
        for (char c : t.toCharArray()) {
            tCount[c]++;
        }

        int required = t.length();
        int left = 0;
        int right = 0;
        int minLen = Integer.MAX_VALUE;
        int minLeft = 0;
        int minRight = 0;

        while (right < s.length()) {
            if (tCount[s.charAt(right)] > 0) {
                required--;
            }
            tCount[s.charAt(right)]--;
            right++;

            while (required == 0) {
                if (right - left < minLen) {
                    minLen = right - left;
                    minLeft = left;
                    minRight = right;
                }

                tCount[s.charAt(left)]++;
                if (tCount[s.charAt(left)] > 0) {
                    required++;
                }
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(minLeft, minRight);
    }
}