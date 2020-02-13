package hard._224;


import org.junit.Assert;
import org.junit.Test;

public class BasicCalculatorTest {
    @Test
    public void testCase1() {
        var input = "1+(2+3)";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);
        try {
            var y = result.parse(x);
            System.out.println(y);
        } catch (Exception e) {
            System.out.print(e);
        }

      //  var tokens = result.tokenize(input);
        Assert.assertEquals(1, 1);


    }
}
