import java.util.Arrays;

class searchRangeFirstandLast {
    public static void main(String[] args) {
        

        searchRangeFirstandLast searchObj = new searchRangeFirstandLast();

        // int[] nums = {5,7,7,8,8,10};
        int[] nums = {4,5,6,7,0,8,8,8,8,1,2};
        int[] res = searchObj.searchRange(nums, 8);
        System.out.println(Arrays.toString(res));
    }


    public static int[] search(int[] nums,)

    public int[] searchRange(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int res[] = new int[2];

        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] == target) {
                int first = mid;
                int last = mid;

                while(first > 0 && nums[first - 1] == target){
                    first--;
                }

                while(last < nums.length - 1 && nums[last + 1] == target){
                    last++;
                }

                return new int[] {first, last}; 
            }

            else if (nums[mid] < target) 
                l = mid + 1;
            else 
                r = mid - 1;

        }
        return new int[] {-1,-1};
    }
}
