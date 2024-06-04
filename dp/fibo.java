import java.util.HashMap;

class fibo {

    public static void main(String[] args) {

        HashMap<Integer, Integer> memo = new HashMap<>();

        for (int i = 0; i < 10; i++) {
                System.out.println(fibo(i, memo));
        }
        
    }

    public static int fibo(int n, HashMap<Integer, Integer> memo) {
        
        if (n <= 1) return n; 

        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        int result = fibo(n-1, memo) + fibo(n-2, memo);

        memo.put(n, result);

        return result;

    }
}
