import java.util.Arrays;

class ProductOfArrayExceptSelf {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        System.out.println(Arrays.toString(productExceptSelf2(nums)));
    }

    public static int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < res.length; i++) {
            res[i] = 1;
        }

        System.out.println(Arrays.toString(res));
        
        for(int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i != j) res[i] *= nums[j];
            }
        }
        
        return res;
    }


    public static int[] productExceptSelf2(int[] nums) {
        
        int[] left_Product = new int[nums.length];
        int[] right_Product = new int[nums.length];
        int n = nums.length;

        left_Product[0] = 1;
        for(int i=1; i<n; i++) {
            left_Product[i] = left_Product[i-1] * nums[i-1];
        }

        right_Product[n-1] = 1;
        for(int i=n-2; i>=0; i--) {
            right_Product[i] = right_Product[i+1] * nums[i+1];
        }

        System.out.println(Arrays.toString(left_Product));
        System.out.println(Arrays.toString(right_Product));

        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            res[i] = left_Product[i] * right_Product[i];
        }

        
        return res;
    }

}




