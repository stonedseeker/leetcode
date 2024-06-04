import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class RepeatingChars {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int size = scanner.nextInt();

        int[] arr = new int[size];

        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        // Code here
        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> repeatingElements = new HashSet<>();

        for (int i : arr) {
            if (!set.add(i)) {
                repeatingElements.add(i);
            }
        }

        for (int element : repeatingElements) {
            System.out.print(element + " ");
        }
        
    }
}

