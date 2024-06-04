import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class CombinationSumii {

    public static void main(String[] args) {
        int[] candidates = {10,1,2,7,6,1,5};
        int target = 8;
        CombinationSumii obj = new CombinationSumii();

        System.out.println(obj.combinationSum2(candidates, target));
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<Integer> list = new ArrayList<>();
        // Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        dfs1(0, target, candidates, list, res);

        return res;
    }

    public static void dfs(int index, int target, int[] nums, List<Integer> list, List<List<Integer>> res) {
        if (index == nums.length) {
            int sum = 0;
            for (Integer i : list) {
                sum += i;
        }

        if (sum == target) {
            res.add(new ArrayList<>(list));
            return;
        } 
        }

        
        if (index >= nums.length || target < 0) return ;

        if (nums[index] <= target) {
            list.add(nums[index]);
            dfs(index + 1, target, nums, list, res);
            list.remove(list.size() - 1);
        }

        dfs(index + 1, target, nums, list, res);
        
   }
    

    public static void dfs1(int index, int target, int[] nums, List<Integer> list, List<List<Integer>> res) {

        if (target == 0) {
            res.add(new ArrayList<>(list));
            System.out.println(res);
            return;
        }

        for (int i = index; i < nums.length; i++) {
            if (i > index && nums[i] == nums[i-1]) continue;
            if (nums[i] > target) break;

            list.add(nums[i]);
            dfs(i+1, target - nums[i], nums, list, res);
            list.remove(list.size() - 1);
        }
    }
}

