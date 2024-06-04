class GCDArray {
    public static void main(String[] args) {
        int[] arr = {7,5,6,8,3};
        GCDArray gcd = new GCDArray();
        System.out.println(gcd.findGCD(arr));
    }

    public int findGCD(int[] nums) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length;i++) {
            if (nums[i] < min) min = nums[i];
            if (nums[i] > max) max = nums[i]; 
        }

        int divisor = min;

        while (max % divisor != 0 || min % divisor != 0) {
            divisor--;
        }
        
        return divisor;
    }
}
