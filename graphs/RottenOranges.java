import java.util.LinkedList;
import java.util.Queue;

class RottenOrages {
    public static void main(String[] args) {
        int[][] grid =  {
                            {0,1,2},
                            {0,1,2},
                            {2,1,1}
                        };

        RottenOrages obj = new RottenOrages();
        int ans = obj.orangesRotten(grid);
        System.out.println(ans);
        
    }

    public int orangesRotten(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int time = 0;
        int countFresh = 0;

        int[][] vis = new int[m][n];

        
        Queue<Pair> q = new LinkedList<Pair>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.add(new Pair(i, j, 0));
                    vis[i][j] = 2;
                } else if (grid[i][j] == 1) {
                    countFresh++;
                }
            }
        }

        int drow[] = {-1, 0, +1, 0};
        int dcol[] = {0, 1, 0, -1}; 
        int cnt = 0;

        while (!q.isEmpty()) {
            Pair p = q.poll();

            int r = p.f;
            int c = p.s;
            int t = p.tm;

            time = Math.max(t, time);


            for (int i = 0; i < 4; i++) {
                int nrow = r + drow[i];
                int ncol = c + dcol[i];

                if (nrow < m && nrow >= 0 && ncol >= 0 && ncol < n
                        && vis[nrow][ncol] == 0 && grid[nrow][ncol] == 1) {
                    q.add(new Pair(nrow, ncol, t + 1));
                    vis[nrow][ncol] = 2;
                    cnt++;

                }
            }

        }

        if (cnt != countFresh) return -1;

        return time;
    }
}


public class Pair {
    int f;
    int s;
    int tm;

    public Pair(int f, int s, int t) {
        this.f = f;
        this.s = s;
        this.tm = t;
    }
}
