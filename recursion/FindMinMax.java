import java.util.Arrays;

class FindMinMax {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6,2213,213,23};
        System.out.println(Arrays.toString(findMinMax(nums, 0, Integer.MIN_VALUE, Integer.MAX_VALUE)));
    }

    public static int[] findMinMax(int[] nums, int count, int max, int min) {
        if (nums.length == count) return new int [] {max, min};

        if (nums[count] > max) max = nums[count]; 
        if (nums[count] < min) min = nums[count];

        return findMinMax(nums, ++count, max, min);
    }
}
