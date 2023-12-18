package easy._020;

import org.junit.jupiter.api.Test;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.assertEquals;

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
            assertEquals(v, result);
        });
    }

    @Test
    public void testCase2() {
        var solution = new ValidParentheses();
        var result = solution.isValid("]");
        assertEquals(false, result);
    }

    @Test
    public void testCase3() {
        var solution = new ValidParentheses();
        var result = solution.isValid("(])");
        assertEquals(false, result);
    }
}
