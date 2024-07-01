import java.util.*;

class Permutations {

    public static void main(String[] args) {
        int[] nums = {1,2,3};
        Permutations obj = new Permutations();
        
        System.out.println(obj.permute(nums));
    }

    public List<List<Integer>> permute(int[] nums) {
        
        class DFS {
            public static void dfs(int start, int[] nums, List<List<Integer>> res) {
                if (start == nums.length) {
                    List<Integer> list = new ArrayList<>();
                    for (int num : nums) {
                        list.add(num);
                    }
                    res.add(new ArrayList<>(list));
                    return;                }

                for (int i = start; i < nums.length; i++) {
                    int temp = nums[i];
                    nums[i] = nums[start];
                    nums[start] = temp;
                    dfs(start + 1, nums, res);
                    temp = nums[i];
                    nums[i] = nums[start];
                    nums[start] = temp;
                }
            }
        }

        List<List<Integer>> res = new ArrayList<>();
        DFS.dfs(0, nums, res);


        return res;
    }

    public List<List<Integer>> permute1(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        class DFS {
            public void dfs(int[] nums, HashMap<Integer, Integer> map, List<Integer> lst, List<List<Integer>> res) {
                if (lst.size() == nums.length) {
                    res.add(new ArrayList<>(lst));
                    return;
                }

                for (int i = 0; i < nums.length; i++) {
                    if (!map.containsKey(nums[i])) {
                        map.put(nums[i], 1);
                        lst.add(nums[i]);
                        dfs(nums, map, lst, res);
                        map.remove(nums[i]);
                        lst.remove(lst.size() - 1);
                    }
                }
            }
        }

        

        List<List<Integer>> res = new ArrayList<>();
        DFS obj = new DFS();
        obj.dfs(nums, map, new ArrayList<>(), res);
        return res;
        
    }

}
