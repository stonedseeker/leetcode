import java.util.ArrayList;

class printMinNumberForPattern {
    public static void main(String[] args) {
        String S = "IIDDD";
        System.out.println(printPatttern(S));
        
    }

    static String printPatttern(String S){
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(1);
        
        for (char c : S.toCharArray()) {
            int m = 0;
            if (c == 'I') {
                m = ans.get(ans.size() - 1);
                while (ans.contains(m)) m++;
                ans.add(m);
            } else {
                ans.add(ans.get(ans.size() - 1));
                for (int i = ans.size() - 1; i > 0; i--) {
                    if (ans.get(i - 1) == ans.get(i)) 
                        ans.set(i - 1, ans.get(i - 1) + 1);;
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (Integer num : ans) {
            result.append(num);
        }


        // Convert StringBuilder to String
        return result.toString();

    }
}
