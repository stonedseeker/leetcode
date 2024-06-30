import java.util.List;
import java.util.HashSet;
import java.util.*;

class SubsetsII {
    public static void main(String[] args) {
        int[] nums = {1, 2, 2};
        System.out.println(subsetsWithDup(nums));
    }

    public static List<List<Integer>> subsetsWithDup(int[] nums) {
        
        Arrays.sort(nums);

        HashSet<List<Integer>> res = new HashSet<>();
        List<Integer> lst = new ArrayList<>();

        
        dfs(0, nums, new ArrayList<>(), res);

        List<List<Integer>> result = new ArrayList<>();
        
        for (List<Integer> i : res) {
            result.add(i);
        }

        return result;
    }

    public static void dfs(int index, int[] nums, List<Integer> lst, HashSet<List<Integer>> res) {
            if (index == nums.length) {
                res.add(new ArrayList<>(lst));
                return;
            }

            lst.add(nums[index]);
            dfs(index + 1, nums, lst, res);
            lst.remove(lst.size() - 1);
            dfs(index + 1, nums, lst, res);
        }

}
