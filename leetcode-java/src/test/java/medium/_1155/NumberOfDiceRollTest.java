package medium._1155;

import org.junit.Assert;
import org.junit.Test;

public class NumberOfDiceRollTest {
    @Test
    public void testCase1() {
        var s= new Solution();
        var actual = s.numRollsToTarget(1, 6, 3);
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase2() {
        var s= new Solution();
        var actual = s.numRollsToTarget(2, 6, 7);
        Assert.assertEquals(actual, 6);
    }

    @Test
    public void testCase3() {
        var s= new Solution();
        var actual = s.numRollsToTarget(2, 5, 10);
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        var s= new Solution();
        var actual = s.numRollsToTarget(1, 2, 3);
        Assert.assertEquals(actual, 0);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.numRollsToTarget(30,30, 500);
        Assert.assertEquals(222616187, actual);
    }

    @Test
    public void testCase6() {
        var s= new Solution();
        var actual = s.numRollsToTarget(3, 3, 6);
        Assert.assertEquals(7, actual);
    }

    @Test
    public void testCase7() {
        var s = new Solution();
        var actual = s.numRollsToTarget(40,40, 600);
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase8() {
        var s = new Solution();
        var actual = s.numRollsToTarget(3,4, 9);
        Assert.assertEquals(10, actual);
    }

    @Test
    public void testCase9() {
        var s = new Solution();
        var actual = s.numRollsToTarget(3,5, 9);
        Assert.assertEquals(19, actual);
    }

    @Test
    public void testCase10() {
        var s = new Solution();
        var actual = s.numRollsToTarget(2,5, 4);
        Assert.assertEquals(3, actual);
    }



}
