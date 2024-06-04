import java.util.*;

class maximumNonAdjacentSum {

    private static int[] memo;

    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(2);
        nums.add(1);
        nums.add(4);
        nums.add(9);

        System.out.println(maximumNonAdjacentSum(nums));
    }

    public static int maximumNonAdjacentSum(ArrayList<Integer> nums) {
        memo = new int[nums.size() + 1];
		return dfs(nums, nums.size() - 1);
	}

	public static int dfs(ArrayList<Integer> nums, int index) {
		if (index == 0) return nums.get(index);
		if (index < 0) return 0;

		if(memo[index]  != 0) return memo[index]; 

		int left = nums.get(index) + dfs(nums, index - 2);
		int right = dfs(nums, index - 1);

		memo[index] = Math.max(left, right);
		return memo[index];
	}



}
