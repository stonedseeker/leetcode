import java.util.ArrayList;

class Subarray {
    public static void main(String[] args) {
        int nums = {1,2,3,4,5};
        System.out.println(subarray(nums));
    }

    public static ArrayList<ArrayList<Integer>> subarray(int[] arr) {

        ArrayList<ArrayList<Integer> list = new ArrayList<>();

        for (int start = 0; start < arr.length; start++) {
            ArrayList<Integer> res = new ArrayList<>();
            for (int end = start; j < arr.length; j++) {
                res.add(arr[j]);
            }
            list.addAll(res);
        }
        return list;
    }
}
