import java.util.ArrayList;
import java.util.List;

public class ElaraAndTheLostEvents {

    public static List<Integer> findPath(int[][] paths) {
        int n = paths.length;
        List<Integer> result = new ArrayList<>();
        boolean[] visited = new boolean[n];

        // Start from node 0
        dfs(paths, 0, visited, result);

        return result;
    }

    private static void dfs(int[][] paths, int node, boolean[] visited, List<Integer> result) {
        visited[node] = true;
        result.add(node);

        for (int neighbor : paths[node]) {
            if (!visited[neighbor]) {
                dfs(paths, neighbor, visited, result);
            }
        }
    }

    public static void main(String[] args) {
        // Test Case 1
        int[][] paths1 = {{1, 2}, {0, 2}, {0, 1}};
        System.out.println("Test Case 1: " + findPath(paths1)); // Expected: [0, 1, 2]

        // Test Case 2
        int[][] paths2 = {{1, 2}, {0, 3}, {0, 3}, {1, 2}};
        System.out.println("Test Case 2: " + findPath(paths2)); // Expected: [0, 1, 2, 3]

        // Test Case 3
        int[][] paths3 = {{1}, {0, 2}, {1}};
        System.out.println("Test Case 3: " + findPath(paths3)); // Expected: [0, 1, 2]

        // Test Case 4
        int[][] paths4 = {{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}};
        System.out.println("Test Case 4: " + findPath(paths4)); // Expected: [0, 1, 2, 3]
    }
}