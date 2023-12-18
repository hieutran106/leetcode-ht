package medium._022_generate_parentheses;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class GenerateParenthesesTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.generateParenthesis(3);
        var expect = Arrays.asList( "((()))",
                "(()())",
                "(())()",
                "()(())",
                "()()()");

        assertEquals(new HashSet<>(actual), new HashSet<>(expect));
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.generateParenthesis(2);
        var expect = Arrays.asList( "()()", "(())");

        assertEquals(new HashSet<>(actual), new HashSet<>(expect));
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.generateParenthesis(4);
        Collections.sort(actual);
        var expect = Arrays.asList( "(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()");
        Collections.sort(expect);
        assertEquals(new HashSet<>(expect), new HashSet<>(actual));
    }
}
