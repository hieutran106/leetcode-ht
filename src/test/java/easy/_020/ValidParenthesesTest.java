package easy._020;

import org.junit.Assert;
import org.junit.Test;

import java.util.HashMap;

public class ValidParenthesesTest {
    @Test
    public void testCase1() {
        var solution = new ValidParentheses();
        var map = new HashMap<String, Boolean>();
        map.put("()", true);
        map.put("()[]{}", true);
        map.put("(]", false);
        map.forEach((k,v) -> {
            var result = solution.isValid(k);
            Assert.assertEquals(v, result);
        });
    }

    @Test
    public void testCase2() {
        var solution = new ValidParentheses();
        var result = solution.isValid("]");
        Assert.assertEquals(false, result);
    }

    @Test
    public void testCase3() {
        var solution = new ValidParentheses();
        var result = solution.isValid("(])");
        Assert.assertEquals(false, result);
    }
}
