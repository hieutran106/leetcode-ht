package hard._224;


import org.junit.Assert;
import org.junit.Test;

public class BasicCalculatorTest {
    @Test
    public void testCase1() {
        var input = "3+2";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 5);
        } catch (Exception e) {
            System.out.print(e);
        }

    }

    @Test
    public void testCase2() {
        var input = "5+3+2";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 10);
        } catch (Exception e) {
            System.out.print(e);
        }
    }

    @Test
    public void testCase3() {
        var input = "5+3-8";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 0);
        } catch (Exception e) {
            System.out.print(e);
        }
    }

    @Test
    public void testCase4() {
        var input = "(5-(3+2))-(3+2)";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, -5);
        } catch (Exception e) {
            System.out.print(e);
        }
    }
    @Test
    public void testCase5() {
        var input = "5-3-2";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 0);
        } catch (Exception e) {
            System.out.print(e);
        }
    }

    @Test
    public void testCase6() {
        var input = "10- (3 - (2-1))-8";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 0);
        } catch (Exception e) {
            System.out.print(e);
        }
    }

    @Test
    public void testCase7() {
        var input = "5 - 3 + 5";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 7);
        } catch (Exception e) {
            System.out.print(e);
        }
    }

    @Test
    public void testCase8() {
        var input = "(1+(4+5+2)-3)+(6+8)";
        BasicCalculator result = new BasicCalculator();

        var x = result.tokenize(input);

        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            Assert.assertEquals(finalResult, 23);
        } catch (Exception e) {
            System.out.print(e);
        }
    }
}
