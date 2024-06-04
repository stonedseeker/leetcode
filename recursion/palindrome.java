class palindrome {
    public static void main(String[] args) {
        // System.out.println(isPalinIter("adssaad"));
        System.out.println(isPalin("raceadsacar", 0));

    }

    public static boolean isPalinIter(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(s.length() - i - 1)) continue;
            else return false;
        }

        return true;
    }

    public static boolean isPalin(String s, int i) {
        if (i >= s.length()/2) return true;

        if (s.charAt(i) != s.charAt(s.length() - 1 - i)) return false;
        return isPalin(s, ++i);
    }
}
