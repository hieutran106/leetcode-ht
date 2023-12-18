package medium._150;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MyTests {
    @Test
    public void testCase1() {
        var solution = new Solution();
        var input = new String[]{"2", "1", "+", "3", "*"};
        var result = solution.evalRPN(input);
        assertEquals(9, result);
    }

    @Test
    public void testCase2() {
        var solution = new Solution();
        var input = new String[]{"4", "13", "5", "/", "+"};
        var result = solution.evalRPN(input);
        assertEquals(6, result);
    }

    @Test
    public void testCase3() {
        var solution = new Solution();
        var input = new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
        var result = solution.evalRPN(input);
        assertEquals(22, result);
    }
}
