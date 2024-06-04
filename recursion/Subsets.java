import java.util.ArrayList;
import java.util.List;

class Subsets {
    public static void main(String[] args) {
        int[] nums = {1,2,5};
        List<Integer> list = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        
        subs(0, nums, list, res);
        System.out.println(res);
    }


    public static void subsWithSum(int index, int[] nums, List<Integer> list, List<List<Integer>> res, int sum) {
        if (index == nums.length) {
            int s = 0;
            for (Integer i : list) {
                s += i;
            }

            if (sum == s)
                res.add(new ArrayList<>(list));
            return;
        }

        list.add(nums[index]);
        subsWithSum(index + 1, nums, list, res, sum);

        list.remove(list.size() - 1);
        subsWithSum(index + 1, nums, list, res, sum);


    }

    public static void subs(int index, int[] nums, List<Integer> list, List<List<Integer>> res) {
        if (index == nums.length) {
            res.add(new ArrayList<>(list));
            return;
        }

        // take 
        list.add(nums[index]);
        subs(index + 1, nums, list, res);
        
        //not take
        list.remove(list.size() - 1);
        subs(index + 1, nums, list, res);
    }
}
