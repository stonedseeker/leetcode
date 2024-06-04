import java.util.Arrays;

class revArr {
    public static void main(String[] args) {
        int[] nums = {1,2,3,5,6,7,8};

        revIter(nums);
        System.out.println(Arrays.toString(nums));

        rev(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));

        oneVarSwap(nums, 0);
        System.out.println(Arrays.toString(nums));
    }

    public static void oneVarSwap(int[] nums, int i) {
        if (i == nums.length / 2) return;
        
        int temp = nums[i];
        nums[i] = nums[nums.length - 1 - i];
        nums[nums.length - 1 - i] = temp;

        oneVarSwap(nums, ++i);


    }


    public static void rev(int[] nums, int l, int r){
        if (l > r) return;

        int temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;

        rev(nums, ++l, --r);
        
    }

    public static void revIter(int[] nums) {
        int l = 0, r = nums.length - 1;

        while (l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }

}
