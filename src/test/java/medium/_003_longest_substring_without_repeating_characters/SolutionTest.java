package medium._003_longest_substring_without_repeating_characters;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("abcabcbb");
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("bbbbb");
        Assert.assertEquals(1, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("pwwkew");
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("");
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("abcdeaabcdef");
        Assert.assertEquals(6, actual);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("aab");
        Assert.assertEquals(2, actual);
    }

    @Test
    public void testCase7() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("dvdf");
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase8() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("advdf");
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase9() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("anviaj");
        Assert.assertEquals(5, actual);
    }

    @Test
    public void testCase10() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("aabcbefefefefpoaj");
        Assert.assertEquals(6, actual);
    }




}