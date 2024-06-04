import java.util.HashMap;
import java.util.PriorityQueue;
// import java.util.StringBuilder;

public class SortCharactersByFrequency {
    public static void main(String[] args) {
       System.out.println(frequencySort("tree")); 
    }

    public static String frequencySort(String s) {

        StringBuilder sb = new StringBuilder();
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i))) {
                map.put(s.charAt(i), 1);
            }
            else map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
        }

        PriorityQueue<Character> q = new PriorityQueue<Character>((a, b) -> map.get(b) - map.get(a));

        q.addAll(map.keySet());

        while (q.size() > 0) {
            char c = q.remove();

            for (int i = 0; i < map.get(c); i++) {
                sb.append(c);
            }
        }

        System.out.println('a' + 1);

        return sb.toString();
    }
}
