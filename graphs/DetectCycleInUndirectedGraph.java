import java.util.*;

class DetectCycleInUndirectedGraph {
    public static void main(String[] args) {
        HashMap<Integer, int[]> map = new HashMap<>();
        map.put(1, new int[] {2,3});
        map.put(2, new int[] {1,5});
        map.put(3, new int[] {1,4,6});
        map.put(6, new int[] {3,7});
        map.put(5, new int[] {2,7});
        map.put(7, new int[] {5,6});

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

        ArrayList<Integer> l0 = new ArrayList<>();
        adj.add(l0);

        ArrayList<Integer> l1 = new ArrayList<>();
        l1.add(2);
        l1.add(3);
        adj.add(l1);

        ArrayList<Integer> l2 = new ArrayList<>();
        l2.add(1);
        l2.add(5);
        adj.add(l2);

        ArrayList<Integer> l3 = new ArrayList<>();
        l3.add(1);
        l3.add(4);
        l3.add(6 );
        adj.add(l3);

        ArrayList<Integer> l4 = new ArrayList<>();
        l4.add(3);
        adj.add(l4);

        ArrayList<Integer> l5 = new ArrayList<>();
        l5.add(2);
        l5.add(7);
        adj.add(l5);

        ArrayList<Integer> l6 = new ArrayList<>();
        l6.add(3);
        l6.add(7);
        adj.add(l6);

        ArrayList<Integer> l7 = new ArrayList<>();
        l7.add(5);
        l7.add(6);
        adj.add(l7);




        for (int i = 0; i < adj.size();i++) {
            System.out.println(i + " " + adj.get(i));
        }


        System.out.println(isCycle(8, adj));
        System.out.println(isCycleDFS(8, adj));

    }
    

    public static boolean isCycleDFS(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean vis[] = new boolean[V];
        for (int i = 0; i < V; i++) vis[i] = false;
        for (int i = 0; i < V; i++) {
            if (vis[i] == false) {
                
                if (dfs(i, -1, vis, adj)) return true;
            }
        }
        return false;
    }

    public static boolean dfs(int node, int parent, boolean[] vis, ArrayList<ArrayList<Integer>> adj) {
        
        
        vis[node] = true;

        for (int adjacentNode: adj.get(node)) {
            if (!vis[adjacentNode]){
                if (dfs(adjacentNode, node, vis, adj)) return true;
            }
            
            else if (adjacentNode != parent) return true;
        }

        return false;

    }




    public static boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        
        boolean[] vis = new boolean[V];
        for (int i = 0; i < V; i++) vis[i] = false;
        for (int i = 0; i < V; i++) {
            if (vis[i] == false) {
                if (checkForCycle(i, V, adj, vis)) return true;
            }
                
        }

        return false;
        
    } 

    public static boolean checkForCycle(int src, int V, ArrayList<ArrayList<Integer>> adj, boolean[] vis) {
        vis[src] = true;
        Queue <int[]> q = new LinkedList<int[]>();

        q.add(new int[] {src, -1});

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int node = temp[0];
            int parent = temp[1];

            for (int adjacentNode : adj.get(node)) {
                if (vis[adjacentNode] == false) {
                    vis[adjacentNode] = true;
                    q.add(new int[] {adjacentNode, node});
                }

                else if (parent != adjacentNode) {
                    return true;
                }

            }
        }
        return false;
        
    }
}
