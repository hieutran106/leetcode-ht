package hard._224;


import org.junit.Assert;
import org.junit.Test;

public class BasicCalculatorTest {
    @Test
    public void testCase1() {
        var input = "1+2+(3-4)+5";
        var result = new BasicCalculator();

        var tokens = result.tokenize(input);
        Assert.assertEquals(1, 1);
    }
}
