package medium._022_generate_parentheses;

import org.junit.Assert;
import org.junit.Test;

public class GenerateParenthesesTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.generateParenthesis(3);
        Assert.assertEquals(actual.size(), 5);
    }

    @Test public void testCase2() {
        var s = new Solution();
        var actual = s.generateParenthesis(2);
        Assert.assertEquals(actual.size(), 2);
    }
}
