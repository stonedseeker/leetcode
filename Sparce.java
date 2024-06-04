import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Sparce {
    public static void main(String[] args) {
        int[][] mat ={
                        {0 , 0 , 3 , 0 , 4 },
                        {0 , 0 , 5 , 7 , 0},
                        {0 , 0 , 0 , 0 , 0 },
                        {0 , 2 , 6 , 0 , 0}
                    };

        for (List<Integer> i : sparce(mat)) {
            System.out.println(i);
        }
    
    }

    public static List<List<Integer>> sparce(int[][] mat) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> row = new ArrayList<>();
        List<Integer> col = new ArrayList<>();
        List<Integer> val = new ArrayList<>();
        
        res.add(row);
        res.add(col);
        res.add(val);


        int m = mat.length;
        int n = mat[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != 0) {
                    res.get(0).add(i);
                    res.get(1).add(j);
                    res.get(2).add(mat[i][j]);
                }
            }
        }

        return res;
    }
}
