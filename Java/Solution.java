import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class Solution {

    public String findFinalCoordinates(String inputString, String key, String initialCoordinates) {
        if (inputString == null || key == null || initialCoordinates == null) {
            throw new IllegalArgumentException("Input string, key, or initial coordinates cannot be null.");
        }

        if (inputString.isEmpty() || key.isEmpty() || initialCoordinates.isEmpty()) {
            throw new IllegalArgumentException("Input string, key, or initial coordinates cannot be empty.");
        }

        if (key.length() != 4 || !key.matches("[NSEW]+")) {
            throw new IllegalArgumentException("Key must be a string of 4 unique characters: N, S, E, W.");
        }

        if (!initialCoordinates.matches("[-+]?[0-9]*\\.?[0-9]+,[-+]?[0-9]*\\.?[0-9]+")) {
            throw new IllegalArgumentException("Invalid initial coordinates format.");
        }

        String[] symbols = inputString.split(" ");
        String[] coordinates = initialCoordinates.split(",");
        double latitude = Double.parseDouble(coordinates[0]);
        double longitude = Double.parseDouble(coordinates[1]);

        for (String symbol : symbols) {
            char direction = symbol.charAt(0);
            int steps = Integer.parseInt(symbol.substring(1));

            int index = key.indexOf(direction);
            switch (index) {
                case 0:
                    latitude += steps;
                    break;
                case 1:
                    latitude -= steps;
                    break;
                case 2:
                    longitude += steps;
                    break;
                case 3:
                    longitude -= steps;
                    break;
            }
        }

        return String.format("%.2f,%.2f", latitude, longitude);
    }
}

class Main {

    Solution solution = new Solution();

    @Test
    void test1() {
        assertEquals("28.00,18.00", solution.findFinalCoordinates("N10 S5 E3 W2", "WENS", "30.00,15.00"), "Test Case 1 Failed");
    }

    @Test
    void test2() {
        assertEquals("25.00,17.00", solution.findFinalCoordinates("E5 W7 N3 S2", "SNWE", "28.00,14.00"), "Test Case 2 Failed");
    }

    @Test
    void test3() {
        assertEquals("35.00,10.00", solution.findFinalCoordinates("S10 N5 W3 E2", "ESWN", "30.00,13.00"), "Test Case 3 Failed");
    }

    @Test
    void test4() {
        assertEquals("20.00,20.00", solution.findFinalCoordinates("N5 E8 S5 W8", "NEWS", "25.00,12.00"), "Test Case 4 Failed");
    }

    @Test
    void testInvalidInputString() {
        try {
            solution.findFinalCoordinates(null, "WENS", "30.00,15.00");
            fail("Expected IllegalArgumentException for null input string.");
        } catch (IllegalArgumentException e) {
            // Expected exception
        }
    }

    @Test
    void testInvalidKey() {
        try {
            solution.findFinalCoordinates("N10 S5 E3 W2", "WENSN", "30.00,15.00");
            fail("Expected IllegalArgumentException for invalid key.");
        } catch (IllegalArgumentException e) {
            // Expected exception
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.test1();
        main.test2();
        main.test3();
        main.test4();
        main.testInvalidInputString();
        main.testInvalidKey();
    }
}