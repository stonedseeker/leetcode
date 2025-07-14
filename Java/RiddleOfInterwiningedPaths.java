import java.util.ArrayList;
import java.util.List;

public class RiddleOfInterwiningedPaths {
   private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
   private static int[][] grid;
   private static boolean[][] visited;
   private static List<String> solutions;
   private static int rows, cols;

   public static List<String> solveRiddle(int[][] grid) {
       RiddleOfInterwiningedPaths.grid = grid;
       rows = grid.length;
       cols = grid[0].length;
       visited = new boolean[rows][cols];
       solutions = new ArrayList<>();

       for (int i = 0; i < rows; i++) {
           for (int j = 0; j < cols; j++) {
               if (grid[i][j] == 1) {
                   backtrack(i, j, new StringBuilder(), 1);
                   visited = new boolean[rows][cols]; // Reset visited array for each starting point
               }
           }
       }

       return solutions;
   }

   private static void backtrack(int row, int col, StringBuilder path, int count) {
       if (count == rows * cols + 1) {
           solutions.add(path.toString());
           return;
       }

       visited[row][col] = true;
       path.append("(" + row + "," + col + ")");

       for (int[] dir : DIRECTIONS) {
           int newRow = row + dir[0];
           int newCol = col + dir[1];

           if (isValid(newRow, newCol) && !visited[newRow][newCol] && grid[newRow][newCol] == 1) {
               backtrack(newRow, newCol, new StringBuilder(path), count + 1);
           }
       }

       visited[row][col] = false;
       path.setLength(path.length() - 4);
   }

   private static boolean isValid(int row, int col) {
       return row >= 0 && row < rows && col >= 0 && col < cols;
   }

   public static void main(String[] args) {
       // Test Case 1
       int[][] grid1 = {{1, 0, 0, 0}, {0, 0, 0, 1}, {0, 0, 1, 0}, {0, 1, 0, 0}};
       List<String> solutions1 = RiddleOfInterwiningedPaths.solveRiddle(grid1);
       System.out.println("Test Case 1 Solutions:");
       for (String solution : solutions1) {
           System.out.println(solution);
       }
       System.out.println();

       // Test Case 2
       int[][] grid2 = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
       List<String> solutions2 = RiddleOfInterwiningedPaths.solveRiddle(grid2);
       System.out.println("Test Case 2 Solutions:");
       for (String solution : solutions2) {
           System.out.println(solution);
       }
       System.out.println();

       // Test Case 3
       int[][] grid3 = {{1, 0}, {0, 1}};
       List<String> solutions3 = RiddleOfInterwiningedPaths.solveRiddle(grid3);
       System.out.println("Test Case 3 Solutions:");
       for (String solution : solutions3) {
           System.out.println(solution);
       }
       System.out.println();

       // Test Case 4
       int[][] grid4 = {{1, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}, {1, 0, 0, 1}};
       List<String> solutions4 = RiddleOfInterwiningedPaths.solveRiddle(grid4);
       System.out.println("Test Case 4 Solutions:");
       if (solutions4.isEmpty()) {
           System.out.println("No valid solution exists");
       } else {
           for (String solution : solutions4) {
               System.out.println(solution);
           }
       }
   }
}
