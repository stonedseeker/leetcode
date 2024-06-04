import java.util.Arrays;

 
class lcs {

    public static void main(String[] args) {
        String a = "longest";
        String b = "stone";
        int m = a.length();
        int n = b.length();
        int[][] dp = new int[m+1][n+1];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = -1;
            }
            
        }
        System.out.println(lcs(a,b, m, n, dp));
    }

    public static int lcs(String a, String b, int m, int n, int[][] dp) {
        if (m == 0 || n == 0)  
            return 0;

        if (a.charAt(m-1) == b.charAt(n-1)) 
            dp[m][n] = 1 + lcs(a,b,m-1,n-1,dp);
        
        else 
            dp[m][n] = Math.max(lcs(a,b,m,n-1,dp), lcs(a,b,m-1,n,dp));
        
        return dp[m][n];
    }



}
