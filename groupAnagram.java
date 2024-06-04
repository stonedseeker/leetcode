import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;

class groupAnagram {
    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"}; 
       System.out.println(groupAnagrams(strs)); 
    }

    static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            // int count = 0;
            // for (int i = 0; i < str.length(); i++) {
            //     count += str.charAt(i) + '0';
            //     map.put(str, count);
            //
            // }
            // if (map.containsKey(count)) {
            //     System.out.println("DO th");
            // }
            
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);

            String sortedStr = new String (charArray);

            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            map.get(sortedStr).add(str);
        }
        System.out.println(map);

        // for (int i = 0; i < map.size(); i++) {
        //     System.out.println(map.get(map.indexOf(i)));
        // i
        
        res.addAll(map.values());
        return res;
    }
}

