import java.util.Scanner;


class LeapYear {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
//Code here
        scanner.close();
        
        isLeapYear(year);
    }
    
    public static void isLeapYear(int year) {
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.print("Leap year");
        } else {
            System.out.print("Not a leap year");
        }
        
    }
}

