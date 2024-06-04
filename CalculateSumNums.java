import java.util.Scanner;

public class CalculateSumNums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String s = scanner.nextLine();
        int sum = 0;
        StringBuilder currentNumber = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                currentNumber.append(c);
            } else {
                if (currentNumber.length() > 0) {
                    sum += Integer.parseInt(currentNumber.toString());
                    currentNumber.setLength(0);
                }
            }
        }

        if (currentNumber.length() > 0) {
            sum += Integer.parseInt(currentNumber.toString());
        }

        System.out.println(sum);
       
    }
}

