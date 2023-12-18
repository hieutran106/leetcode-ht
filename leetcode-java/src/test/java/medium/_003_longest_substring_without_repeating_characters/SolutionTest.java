package medium._003_longest_substring_without_repeating_characters;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class SolutionTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("abcabcbb");
        assertEquals(3, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("bbbbb");
        assertEquals(1, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("pwwkew");
        assertEquals(3, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("");
        assertEquals(0, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("abcdeaabcdef");
        assertEquals(6, actual);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("aab");
        assertEquals(2, actual);
    }

    @Test
    public void testCase7() {
        var s = new Solution();
        var actual = s.lengthOfLongestSubstring("dvdf");
        assertEquals(3, actual);
    }

    @Test
    public void testCase8() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("advdf");
        assertEquals(3, actual);
    }

    @Test
    public void testCase9() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("anviaj");
        assertEquals(5, actual);
    }

    @Test
    public void testCase10() {
        var s = new Solution();
        var actual  = s.lengthOfLongestSubstring("aabcbefefefefpoaj");
        assertEquals(6, actual);
    }




}