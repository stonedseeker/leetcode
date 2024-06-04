import java.util.Arrays;

class mergeSorted {
    public static void main(String[] args) {
       int[] a1 = {1,2,3,0,0,0};
       int[] a2 = {2,5,6};
       merge(a1,a2,3,3);
       System.out.println(Arrays.toString(a1));
    }

    public static void merge(int[] a1, int[] a2, int m, int n) {
        
        for (int i = 0, j = 0; i < a1.length && j < a2.length;) {
            if (a1[i] > a2[j]) {
                int temp = a1[i];
                a1[i] = a2[j];
                a1[m + j] = temp; 
                i++;
                j++;
            }

            if (a1[i] == 0) {
                a1[i] = a2[j];
                j++;
            }

            i++; 
        }
        System.out.println(Arrays.toString(a1));
    }
}
