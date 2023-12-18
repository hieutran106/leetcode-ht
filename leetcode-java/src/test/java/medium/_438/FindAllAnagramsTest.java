package medium._438;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

public class FindAllAnagramsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.findAnagrams("cbaebabacd", "abc");
        int[] array = result.stream().mapToInt(i -> i).toArray();
        assertArrayEquals(new int[]{0, 6}, array);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.findAnagrams("abab", "ab");
        int[] array = result.stream().mapToInt(i -> i).toArray();
        assertArrayEquals(new int[]{0,1, 2}, array);
    }
}
