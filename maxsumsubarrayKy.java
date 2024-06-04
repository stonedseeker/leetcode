import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;

class maxsumsubarrayKy{
    public static void main(String[] args) {
       ArrayList<Integer> list = new ArrayList<>(); 
        
       list.add(400);
       list.add(200);
       list.add(300);
       list.add(600);
       

       ///etc/fancontrol
       ///etc/fancontrol
       //400 200 300 100

       
       System.out.println(maximumSumSubarray(2, list, 4));

    }

    static long maximumSumSubarray(int K, ArrayList<Integer> Arr,int N){
        long sum = 0, res = 0;
        int i = 0, j = 0;

        while (j != K) {
            sum += Arr.get(j++);
            j++;
    }
        res = sum; 

        while( j!= N) {
            sum += Arr.get(j++);
            sum -= Arr.get(i++);

            res = Math.max(res, sum);
        }

          
        return res;
    }
}
