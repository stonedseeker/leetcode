import java.util.ArrayList;
import java.util.Arrays;

class MergeSort {
    public static void main(String[] args) {
        int[] nums = {3,1,2,4,1,5,6,2,4};
        mergeSort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }

    public static void mergeSort(int[] nums, int l, int r) {
        if (l >= r) return;

        int mid = (l + r) / 2;
        
        mergeSort(nums, l, mid);
        mergeSort(nums, mid + 1, r);
        merge(nums, l, mid, r);

    }

    public static void merge(int[] nums, int l, int mid, int r) {
        ArrayList<Integer> merged = new ArrayList<>();

        int left = l;
        int right = mid + 1;

        while (left <= mid && right <= r) {
            if (nums[left] < nums[right]) {
                merged.add(nums[left]);
                left++;
            } else {
                merged.add(nums[right]);
                right++;
            }
                
        }

        while (left <= mid) {
            merged.add(nums[left]);
            left++;
        }

        while (right <= r) {
            merged.add(nums[right]);
            right++;
        }

        for (int i = l; i <= r; i++) {
            nums[i] = merged.get(i-l);
        }
    }
}
