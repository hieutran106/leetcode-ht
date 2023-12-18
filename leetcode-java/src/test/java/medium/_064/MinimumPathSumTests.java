package medium._064;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.Arrays;

public class MinimumPathSumTests {

    private MinimumPathSumSolution solution() {
        return new MinimumPathSumDP();
    }
    @Test
    public  void testCase1() {
        int[][] input = {
                {1,3,1},
                {1,5,1},
                {4,2,1}
        };
        var solution = solution();
        var result = solution.minPathSum(input);
        assertEquals(7, result);
    }

    @Test
    public void testCase2() {
        int[][] input = {
                {1,2,5},
                {3,2,1},

        };
        var solution = solution();
        var result = solution.minPathSum(input);
        assertEquals(6, result);
    }

    @Test
    public void testCase3() throws FileNotFoundException, IOException {

        FileInputStream fs = new FileInputStream("src/test/resources/medium_064_input.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(fs));
        String strLine;
        int[][] input = new int[200][200];
        int count = 0;
        while ((strLine = br.readLine()) != null) {
            var test = Arrays.stream(strLine.split(" ")).map(x -> Integer.parseInt(x)).toArray();
            for (int i =0; i < test.length; i ++) {
                input[count][i] = (int)test[i];
            }
            count ++;
        }

        fs.close();
        var solution = solution();
        var result = solution.minPathSum(input);
        System.out.println(result);
        assertEquals(823, result);
    }
}
