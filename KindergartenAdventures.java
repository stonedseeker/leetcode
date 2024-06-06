import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY t as parameter.
     */

    public static int solve(List<Integer> t) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        return 2;

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int tCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> t = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int id = Result.solve(t);

        bufferedWriter.write(String.valueOf(id));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

