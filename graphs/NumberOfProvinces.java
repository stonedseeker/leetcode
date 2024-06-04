class NumberOfProvinces {
    public static void main(String[] args) {
    
        int[][] isConnected =   {
                                    {1,1,0},
                                    {1,1,0},
                                    {0,0,1}
                                };

        System.out.println(findCircleNum(isConnected));
    }


    public static int findCircleNum(int[][] isConnected) {
        boolean[] vis = new boolean[isConnected.length];
        int res = 0;

        for (int i = 0; i < isConnected.length; i++) {
            if (!vis[i]) {
                res++;
                dfs(isConnected, vis, i);
            }
        }

        return res;
    }

    public static void dfs(int[][] isConnected, boolean[] vis, int node) {
        if (!vis[node]) {
            vis[node] = true;
            for (int j = 0; j < isConnected[node].length;j++) {
                if (isConnected[node][j] == 1){
                    dfs(isConnected, vis, j);
                }
            }
        }
    }




}
