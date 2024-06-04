import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;


class permutations {
    public static void main(String[] args) {
        int[] nums = {1,2,3};
        List<List<Integer>> res = new ArrayList<>();
        dfs(0, nums, res);
        System.out.println(res);
    }

    public static void dfs(int index, int[] nums, List<List<Integer>> res) {

        
        if (index == nums.length) {
            // res.add(new ArrayList<>(list));
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                list.add(nums[i]);
            }
            res.add(new ArrayList<>(list));
            return;
        }


        for (int i = index; i < nums.length; i++) {
            swap(nums, i, index);
            dfs(index+1, nums, res);
            swap(nums, i, index);
        }
    }

    public static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        System.out.println(Arrays.toString(nums));
    }

    public static void dfs1(int[] nums, List<Integer> list, List<List<Integer>> res, boolean[] freq) {

        if (list.size() == nums.length) {
            res.add(new ArrayList<>(list));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!freq[i]) {
                freq[i] = true;
                list.add(nums[i]);
                dfs1(nums, list, res, freq);
                list.remove(list.size() -1); 
                freq[i] = false;
            }
            
        }

    }
}
