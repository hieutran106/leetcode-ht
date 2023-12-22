package easy._1422_maximum_score_after_splitting_string;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class SolutionTest {
    public static class Solution {
        public int maxScore(String s) {
            int rightOne = 0;
            for (int i =0; i < s.length(); i++) {
                if (s.charAt(i) == '1') {
                    rightOne++;
                }
            }
            int maxScore = 0;
            int leftZero = 0;
            for (int i =0; i < s.length() - 1; i++) {
                if (s.charAt(i) == '0') {
                    leftZero++;
                } else {
                    rightOne--;
                }

                maxScore = Math.max(maxScore, leftZero + rightOne);
            }
            return maxScore;
        }
    }

    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.maxScore("011101");
        Assertions.assertEquals(5, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.maxScore("00111");
        Assertions.assertEquals(5, actual);
    }
    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.maxScore("1111");
        Assertions.assertEquals(3, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.maxScore("01");
        Assertions.assertEquals(2, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.maxScore("10");
        Assertions.assertEquals(0, actual);
    }
}