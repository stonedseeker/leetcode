import java.util.*;

class maxSlidingWindow {
    public static void main(String[] args) {
     int[] nums = {1,3,-1,-3,5,3,6,7};
     System.out.println(Arrays.toString(maxSlidingWindow(nums, 3)));

    }

    public static int[] maxSlidingWindow(int[] nums, int k) {
        
        List<Integer> lst = new ArrayList<Integer>();


        for (int l = 0, r = k - 1;  r < nums.length; l++, r++) {
            int i = l;
            while (i <= r) {
                System.out.print(nums[i] + " ");
                i++;
            }
            System.out.println();
            int max = findMax(nums, l, r);
            lst.add(max);
        }

        System.out.println(lst);
        int[] res = new int[lst.size()];
        for (int i = 0; i < lst.size();i++) {
            res[i] = lst.get(i);
        }
        return res;
    }

    public static int findMax(int[] nums, int l, int r) {
        int max = Integer.MIN_VALUE;
        for (int i = l; i <= r; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }

        return max;
    }
}
