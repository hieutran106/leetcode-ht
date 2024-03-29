package medium._005;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

public class LongestPalindromeTests {

    @Test
    public void testIsPalindrome1() {
        var solution = new Solution();
        var result = solution.isPalindrome1(1, "abba", false);
        assertArrayEquals(result, new int[]{0, 3});
    }

    @Test
    public void testIsPalindrome2() {
        var solution = new Solution();
        var result = solution.isPalindrome1(1, "cdc", true);
        System.out.println(Arrays.toString(result));
        assertArrayEquals(result, new int[]{0, 2});
    }

    @Test
    public void testIsPalindrome3() {
        var solution = new Solution();
        var result = solution.isPalindrome1(1, "abbc", false);

        assertArrayEquals(result, new int[] {1, 2});
    }

    @Test
    public void testCase1() {
        var solution = new Solution();
        var result = solution.longestPalindrome("babad");
        System.out.println(result);

        assertTrue(result.equals("bab") || result.equals("aba"));
    }

    @Test
    public void testCase2() {
        var solution = new Solution();
        var result = solution.longestPalindrome("cbbd");
        System.out.println(result);
        assertEquals(result, "bb");
    }

    @Test
    public void testCase3() {
        var solution = new Solution();
        var result = solution.longestPalindrome("");
        System.out.println(result);
        assertEquals(result, "");
    }

    @Test
    public void testCase4() {
        var solution = new Solution();
        var result = solution.longestPalindrome("abcd1234321ghikabcdeffedcbatretoirt");
        System.out.println(result);
        assertEquals(result, "abcdeffedcba");
    }

    @Test
    public void testCase5() {
        var solution = new Solution();
        var result = solution.longestPalindrome("a");
        System.out.println(result);
        assertEquals(result, "a");
    }

    @Test
    public void testCase6() {
        var solution = new Solution();
        var result = solution.longestPalindrome("abcdef");
        System.out.println(result);
        assertEquals(result, "a");
    }

    @Test
    public void testCase7() {
        var solution = new Solution();
        var result = solution.longestPalindrome("bb");
        System.out.println(result);
        assertEquals(result, "bb");
    }
}
