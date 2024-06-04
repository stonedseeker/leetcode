import java.util.Arrays;

class shuffleArray{
    public static void main(String[] args){
        int[] arr = {1,9,2,15};
        System.out.println(Arrays.toString(shuffle(arr)));
    
    }

    public static int[] shuffle(int[] arr) {
        int[] res = new int[arr.length];

        
        for(int i = 0, mid = arr.length / 2; mid < arr.length; i+=2, mid++){
            res[i] = arr[i];
            res[i+1] = arr[mid];
        }

        return res;
    }
}
