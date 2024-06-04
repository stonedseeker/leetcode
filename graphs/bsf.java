import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class bsf {
    public static void main(String[] args) {
        // 1 
        // 2 6
        // 3 4 7 9
        // 5 8
        ArrayList<Integer> one = new ArrayList<>();
        one.add(1);
        ArrayList<Integer> two = new ArrayList<>();
        two.add(2);
        two.add(6);
        ArrayList<Integer> thr = new ArrayList<>();
        thr.add(3);
        thr.add(4);
        thr.add(7);
        thr.add(9);
        ArrayList<Integer> four = new ArrayList<>();
        four.add(5);
        four.add(8);
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        graph.add(one);
        graph.add(two);
        graph.add(thr);
        graph.add(four);

        for (int i = 0; i < graph.size(); i++) {
            System.out.println(graph.get(i));
        }

        ArrayList<ArrayList<Integer>> res = bfsOfGraph(4, graph);

        for (ArrayList<Integer> list : res) {
            System.out.println(list);
        }

    }

    public static ArrayList<ArrayList<Integer>> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        boolean[] vis = new boolean[V];

        Queue<ArrayList<Integer>> q = new LinkedList<>();
        q.add(adj.get(0));

        while (!q.isEmpty()) {
            int levelSize = q.size();
            ArrayList<Integer> level = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                int node = q.poll();
                level.add(node); // Add 1 to convert back to 1-based index

                for (Integer neighbor : adj.get(node)) {
                    if (!vis[neighbor - 1]) {
                        vis[neighbor - 1] = true;
                        q.add(neighbor - 1);
                    }
                }
            }

            result.add(level);
        }

        return result;


        // ArrayList<Integer> bfs = new ArrayList<>();
        // boolean vis[] = new boolean[V];
        //
        // Queue<ArrayyList<Integer>> q = new LinkedList<>();
        //
        // q.add(graph.get(0));
        // vis[0] = true;
        


        // while (!q.isEmpty()) {
        //     Integer node = q.poll();
        //     bfs.add(node + 1);
        //
        //     for (Integer it: adj.get(node)) {
        //         if (it < V && vis[it] == false){
        //             vis[it] = true;
        //             q.add(it);
        //         }
        //     }
        // }
        
        // while(!q.isEmpty()) {
        //     int size = q.size();
        //     ArrayList<Integer> level = q.poll();
        //     for (Integer node : level) {
        //         Integer node = q.poll();
        //         bfs.add(node + 1);
        //
        //         for (Integer neighbour : adj.get(node)) {
        //             if (!vis[neighbour - 1]) {
        //                 vis[neighbour - 1] = true;
        //                 q.add(neighbour - 1);
        //             }
        //         }
        //     }
        // }
    }
}
