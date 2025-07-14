public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test Case 1
        int[] symbols1 = {1, 2, 3, 4, 5};
        int key1 = 3;
        int expected1 = 0;
        assert  solution.unlockGate(symbols1, key1) == expected1 : "Test Case 1 Failed";

        // Test Case 2
        int[] symbols2 = {5, 1, 2, 3, 4};
        int key2 = 2;
        int expected2 = 1;
        assert  solution.unlockGate(symbols2, key2) == expected2 : "Test Case 2 Failed";

        // Test Case 3
        int[] symbols3 = {10, 5, 2, 7, 1};
        int key3 = 4;
        int expected3 = 2;
        assert  solution.unlockGate(symbols3, key3) == expected3 : "Test Case 3 Failed";

        // Test Case 4
        int[] symbols4 = {2, 4, 6, 8, 10};
        int key4 = 2;
        int expected4 = 3;
        assert  solution.unlockGate(symbols4, key4) == expected4 : "Test Case 4 Failed";

        // Exception Test Case 1 (null input)
        try {
            solution.unlockGate(null, 2); 
            System.err.println("Exception Test Case 1 Failed (null input)"); 
        } catch (IllegalArgumentException e) {
            // Exception caught as expected
        }

        // Exception Test Case 2 (invalid key)
        try {
            solution.unlockGate(symbols1, 0);
            System.err.println("Exception Test Case 2 Failed (invalid key)"); 
        } catch (IllegalArgumentException e) {
            // Exception caught as expected
        }
    }
}


class Solution {
    public int unlockGate(int[] symbols, int key) {
        if (symbols == null || symbols.length == 0 || key <= 0 || key > symbols.length) {
            throw new IllegalArgumentException("Invalid input parameters.");
        }

        int n = symbols.length;
        int maxSum = Integer.MIN_VALUE;
        int minRotations = 0;

        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            for (int j = 0; j < key; j++) {
                currentSum += symbols[(i + j) % n]; 
            }

            if (currentSum > maxSum) {
                maxSum = currentSum;
                minRotations = i;
            }
        }

        return minRotations;
    }
}

