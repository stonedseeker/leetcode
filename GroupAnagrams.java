import java.util.*;

class GroupAnagrams {
    public static void main(String[] args) {
        String[] strs = {"tan", "ant", "nat", "bat", "ate", "tea", "eat"};
        System.out.println(groupAnagrams(strs));
    }

    public static List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            String base = base(str);
            System.out.println("base = " + base);
            
            if (!map.containsKey(base)) {
                map.put(base, new ArrayList<>());
            }

            map.get(base).add(str);
        }

        return new ArrayList<>(map.values());

    }

    public static String base(String str) {
        char[] base = str.toCharArray();
        Arrays.sort(base);
        String res = new String(base);
        return res;
            
    }

    
}
