package medium._907_sum_of_subarray_minimums;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.function.DoubleToIntFunction;
import java.util.stream.Stream;


public class SolutionTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.sumSubarrayMins(new int[]{3, 1, 2, 4});
        Assert.assertEquals(actual, 17);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.sumSubarrayMins(new int[]{1, 2});
        Assert.assertEquals(actual, 4);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.sumSubarrayMins(new int[]{1});
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.sumSubarrayMins(new int[]{3, 2, 2, 3});
        Assert.assertEquals(actual, 22);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.sumSubarrayMins(new int[]{71, 55, 82, 55});
        Assert.assertEquals(actual, 593);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        try {
            Path inputPath = Path.of("./src/test/java/medium/_907_sum_of_subarray_minimums/input.txt");
            String numbers = Files.readString(inputPath);
            String[] stringArray = numbers.split(" ");
            int[] input = Stream.of(stringArray).mapToInt(Integer::parseInt).toArray();
            var actual = s.sumSubarrayMins(input);
            Assert.assertEquals( 667452382, actual);
        } catch (IOException e) {
            System.out.println("Input Not Found");
        }

    }
}