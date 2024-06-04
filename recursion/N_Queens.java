import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class N_Queens {
    public static void main(String[] args) {
        
        for (List<String> i : solveNQueens(4)) {
                System.out.println(i);
                System.out.println();
            }
        
    }

    public static List<List<String>> solveNQueens(int n) {
        
        List<String> board = new ArrayList<>(); 
        for (int i = 0; i < n; i++) {
            board.add("....");  
        } 

        System.out.println(board);
        List<List<String>> res = new ArrayList<>();
        solve(0, board,res,n);

        return res;
    } 
    
    public static boolean isSafe(int row, int col, List<String> board, int n) {
    int drow = row;
    int dcol = col;

    while (row >= 0 && col >= 0) {
        if (board.get(row).charAt(col) == 'Q') return false;
        row--; col--;
    }

    row = drow;
    col = dcol;

    while (col >= 0) {
        if (board.get(row).charAt(col) == 'Q') return false;
        col--;
    }

    col = dcol;

    while (row < n && col >= 0) {
        if (board.get(row).charAt(col) == 'Q') return false;
        row++; col--;
    }

    return true;
}



    public static void solve(int row, List<String> board, List<List<String>> res, int n) {
        if (row == n){
            // List<String> cop y = new ArrayList<>(board);            
            res.add(new ArrayList<String>(board));
            return;
        }

        for (int col = 0; col < n; col++) {
            if (board.get(row).charAt(col) == '.' && isSafe(row, col, board, n)) {
                // Convert the string to a character array
                char[] charArray = board.get(row).toCharArray();
                charArray[col] = 'Q'; // Modify the character array
                board.set(row, new String(charArray)); // Convert the character array back to a string
                solve(row + 1, board, res, n);
                charArray[col] = '.'; // Restore the character array
                board.set(row, new String(charArray)); // Convert the character array back to a string
            }
    }


        
    }


}
