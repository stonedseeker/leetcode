import java.util.Arrays;

class SumTriangle {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5};
        sumTriangle(nums);

    }

    public static void sumTriangle(int[] nums ) {
        if (nums.length < 1) return;

        int[] temp = new int[nums.length - 1];

        for (int i = 0; i < nums.length - 1; i++) {
            temp[i] = nums[i] + nums[i + 1];
        }

        sumTriangle(temp);

    
        System.out.println(Arrays.toString(nums));
    } 
}
