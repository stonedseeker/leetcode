import java.util.*;

public class IntertwinedPathsSolver {
    
    public static List<Integer> solveIntertwinedPaths(int n, List<int[]> paths) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] path : paths) {
            graph.putIfAbsent(path[0], new ArrayList<>());
            graph.putIfAbsent(path[1], new ArrayList<>());
            graph.get(path[0]).add(path[1]);
            graph.get(path[1]).add(path[0]);
        }

        // Check for Eulerian Circuit (all vertices must have even degree)
        for (int node : graph.keySet()) {
            if (graph.get(node).size() % 2 != 0) {
                return new ArrayList<>();
            }
        }

        // Hierholzer's algorithm to find Eulerian Circuit
        List<Integer> circuit = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(paths.get(0)[0]);

        while (!stack.isEmpty()) {
            int current = stack.peek();
            if (!graph.get(current).isEmpty()) {
                int next = graph.get(current).remove(0);
                graph.get(next).remove((Integer) current);
                stack.push(next);
            } else {
                circuit.add(stack.pop());
            }
        }

        return circuit;
    }

    public static void main(String[] args) {
        List<int[]> testCase1 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3});
        List<int[]> testCase2 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 0});
        List<int[]> testCase3 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3});
        List<int[]> testCase4 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3}, new int[]{3, 4}, new int[]{4, 5}, new int[]{5, 0});
        
        // Additional Test Cases
        List<int[]> testCase5 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3}, new int[]{3, 0}, new int[]{0, 2}, new int[]{1, 3});
        List<int[]> testCase6 = Arrays.asList(new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3}, new int[]{3, 4}, new int[]{4, 5}, new int[]{5, 6}, new int[]{6, 0}, new int[]{1, 5});
        
        System.out.println("Test Case 1: " + solveIntertwinedPaths(4, testCase1));
        System.out.println("Test Case 2: " + solveIntertwinedPaths(3, testCase2));
        System.out.println("Test Case 3: " + solveIntertwinedPaths(5, testCase3));
        System.out.println("Test Case 4: " + solveIntertwinedPaths(6, testCase4));
        System.out.println("Test Case 5: " + solveIntertwinedPaths(4, testCase5));
        System.out.println("Test Case 6: " + solveIntertwinedPaths(7, testCase6));
    }
}
