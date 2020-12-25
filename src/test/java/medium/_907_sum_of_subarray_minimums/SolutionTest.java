package medium._907_sum_of_subarray_minimums;

import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.stream.Stream;


public class SolutionTest {
    @Test
    public void testCase1() {
        var s = new Solution2();
        var actual = s.sumSubarrayMins(new int[]{3, 1, 2, 4});
        Assert.assertEquals(actual, 17);
    }

    @Test
    public void testCase2() {
        var s = new Solution2();
        var actual = s.sumSubarrayMins(new int[]{1, 2});
        Assert.assertEquals(actual, 4);
    }

    @Test
    public void testCase3() {
        var s = new Solution2();
        var actual = s.sumSubarrayMins(new int[]{1});
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        var s = new Solution2();
        var actual = s.sumSubarrayMins(new int[]{3, 2, 2, 3});
        Assert.assertEquals(actual, 22);
    }

    @Test
    public void testCase5() {
        var s = new Solution2();
        var actual = s.sumSubarrayMins(new int[]{71, 55, 82, 55});
        Assert.assertEquals(actual, 593);
    }

    @Test
    public void testCase6() {
        var s = new Solution2();
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



    @Test
    public void testCase8() {
        var s= new Solution2();
        var actual = s.previousSmallerRange(new int[]{6, 2, 9, 4, 3, 1, 5});
        System.out.println(Arrays.toString(actual));
        Assert.assertArrayEquals(new int[]{1, 2, 1, 2, 3, 6, 1}, actual);
    }
    @Test
    public void testCase10() {
        var s= new Solution2();
        var actual = s.previousSmallerRange(new int[]{3, 1, 2, 4});
        Assert.assertArrayEquals(new int[]{1, 2, 1, 1}, actual);
    }

    @Test
    public void testCase9() {
        var s= new Solution2();
        var actual = s.nextSmallerElementRange(new int[]{3, 1, 2, 4});
        System.out.println(Arrays.toString(actual));
        Assert.assertArrayEquals(new int[]{1, 3, 2, 1}, actual);
    }

    @Test
    public void testCase7() {
        var s= new Solution2();
        var actual = s.nextSmallerElementRange(new int[]{6, 2, 9, 4, 3, 1, 5});
        System.out.println(Arrays.toString(actual));
        Assert.assertArrayEquals(new int[]{1, 4, 1, 1, 1, 2 , 1}, actual);
    }


}