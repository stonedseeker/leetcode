class LargestSmallSum {
    public static void main(String[] args) {
        int[] arr = {5,2,4,3,9,7,1};
        System.out.println(largestSmallSum(arr));
    }

    public static int largestSmallSum(int[] nums) {
        int l = Integer.MIN_VALUE;
        int sl = Integer.MIN_VALUE;
        int s = Integer.MAX_VALUE;
        int ss = Integer.MAX_VALUE;
        for (int i = 0, j = 1; i < nums.length && j < nums.length; i+=2, j+=2) {
            if (nums[i] > l){
                    sl = l;
                    l = nums[i];
            }
                else {
                    sl = nums[i];
                }
            

            if (nums[j] < s) {
                    int temp = s;
                    ss = s;
                    s = nums[j];
                    
                }else {
                    ss = nums[j];
                }
        }
        System.out.println(sl + " " + ss );

        return sl + ss;
    }
}
