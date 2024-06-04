import java.io.*;
import java.util.*;

public class BabyMonty{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the number of test cases
        int t = scanner.nextInt();

        while (t-- > 0) {
            // Read the number of nodes in the graph
            int n = scanner.nextInt();

            // Create an adjacency list to represent the graph
            List<List<Integer>> adjList = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                adjList.add(new ArrayList<>());
            }

            // Read the edges of the graph
            for (int i = 1; i < n; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                
                // Add edges to the adjacency list
                adjList.get(u).add(v);
                adjList.get(v).add(u);
            }

            // Perform operations with the graph as required
            
            // Example: Print the adjacency list
            for (int i = 1; i <= n; i++) {
                System.out.print(i + " -> ");
                for (int neighbor : adjList.get(i)) {
                    System.out.print(i + " = " + neighbor + " ");
                }
                System.out.println();
            }

            Queue<List<Integer>> q = new LinkedList<>();
            int count = 0;
            
            for (int index = 1; index < adjList.size(); index++) {

                q.offer(adjList.get(index));

                while (!q.isEmpty()) {
                    int qLen = q.size();
                    for (int i = 0; i < qLen; i++) {
                        List<Integer> temp = q.poll();
                        System.out.print(i + " " + temp);
                        q.add(temp);
                    }
                }
            }
        }

        // Close the scanner
        scanner.close();
    }
}
