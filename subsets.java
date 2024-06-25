import java.util.*;

class subsets {
    public static void main(String[] args) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> nums = new ArrayList<>();

        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        
        subs(0, res, new ArrayList<>(), nums);
        System.out.println(res);
    }

    public static void subs(int index, List<List<Integer>> res, List<Integer> lst, List<Integer> nums) {
        if (index == nums.size()) {
            res.add(new ArrayList<>(lst));
            return;
        }

        lst.add(nums.get(index));
        subs(index + 1, res, lst, nums);
        lst.remove(lst.size() - 1);
        subs(index + 1, res, lst, nums);


    } 
}
