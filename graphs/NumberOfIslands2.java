class NumberOfIslands2 {
    public static void main(String[] args) {
        char[][] grid = {
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}
        };

        System.out.println(numIslands(grid));
    }

    public static int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int res = 0 ;

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == '1') {
                    res++;
                    dfs(grid, row, col);
                }
            }
        }

        return res;
    }

    public static void dfs(char[][] grid, int row, int col) {
        
        int m = grid.length; 
        int n = grid[0].length;

        if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == '0') return;
        grid[row][col] = '0';

        dfs(grid, row + 1, col);
        dfs(grid, row - 1, col);
        dfs(grid, row, col + 1);
        dfs(grid, row, col - 1);
                
    }
}
