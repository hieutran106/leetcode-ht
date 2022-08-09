package hard._224;


import org.junit.Assert;
import org.junit.Test;

public class SolutionBacktracking2Test {
    @Test
    public void testCase1() {
        var input = "3+2";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 5);

    }

    @Test
    public void testCase2() {
        var input = "5+3+2";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);

        Assert.assertEquals(finalResult, 10);

    }

    @Test
    public void testCase3() {
        var input = "5+3-8";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 0);
    }

    @Test
    public void testCase4() {
        var input = "(3+(3+3))-(6+3)";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 0);
    }
    @Test
    public void testCase5() {
        var input = "5-3-2";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 0);
    }

    @Test
    public void testCase6() {
        var input = "10- (3 - (2-1))-8";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 0);

    }

    @Test
    public void testCase7() {
        var input = "5 - 3 + 5";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 7);

    }

    @Test
    public void testCase8() {
        var input = "(1+(4+5+2)-3)+(6+8)";
        Solution2 s = new Solution2();
        var finalResult = s.calculate(input);
        Assert.assertEquals(finalResult, 23);
    }
}
