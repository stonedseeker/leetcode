import  java.util.Arrays;

class MedianSortedArray {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};

        System.out.println(findMedianSortedArrays(nums1, nums2));
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length + nums2.length];
        int i = 0, j = 0, k = 0;
        for (i = 0, j = 0; i < nums1.length && j < nums2.length;) {
            if (nums1[i] < nums2[j]) {
                res[k] = nums1[i];
                i++;
                k++;
            } else {
                res[k] = nums2[j];
                j++;
                k++;
            }
        }

        while (i < nums1.length) {
            res[k] = nums1[i];
            k++;
            i++;
        }

        while (j < nums2.length) {
            res[k] = nums2[j];
            k++;
            j++;
        }

        System.out.println(Arrays.toString(res));


        if (res.length % 2 == 1){
            return res[res.length / 2];
        } else {
            System.out.println(res[(res.length / 2)]);
            System.out.println(res[(res.length / 2) - 1]);
            double val = res[(res.length / 2) - 1] + res[(res.length / 2)];
            return val / 2;
        }

        
    }
}
