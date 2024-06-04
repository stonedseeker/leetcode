import java.util.*;

class BSFArray {
    public static void main(String[] args) {
        int[][] adj = {
            {0}, 
            {2,6},
            {1,3,4},
            {2},
            {2,5},
            {4,8},
            {1,7,9},
            {6,8},
            {5,7},
            {6}
        };
        
        int[] vis = new int[adj.length];

        bsfArr(adj, 1, vis);
    }

    public static void bsfArr(int[][] adj, int startNode, int[] vis) {
        
        Queue<Integer> q = new LinkedList<>();
        q.add(startNode);
        vis[startNode] = 1;

        while(!q.isEmpty()) {
            
            int node = q.poll();
            System.out.println(node);

            for (int neighbour : adj[node]) {
                if (vis[neighbour] != 1) {
                    vis[neighbour] = 1;
                    q.add(neighbour);
                }
            }
        }
    }
}
