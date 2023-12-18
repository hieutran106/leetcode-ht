package medium._1155;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class NumberOfDiceRollTest {
    @Test
    public void testCase1() {
        var s= new Solution();
        var actual = s.numRollsToTarget(1, 6, 3);
        assertEquals(actual, 1);
    }

    @Test
    public void testCase2() {
        var s= new Solution();
        var actual = s.numRollsToTarget(2, 6, 7);
        assertEquals(actual, 6);
    }

    @Test
    public void testCase3() {
        var s= new Solution();
        var actual = s.numRollsToTarget(2, 5, 10);
        assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        var s= new Solution();
        var actual = s.numRollsToTarget(1, 2, 3);
        assertEquals(actual, 0);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.numRollsToTarget(30,30, 500);
        assertEquals(222616187, actual);
    }

    @Test
    public void testCase6() {
        var s= new Solution();
        var actual = s.numRollsToTarget(3, 3, 6);
        assertEquals(7, actual);
    }


    @Test
    public void testCase8() {
        var s = new Solution();
        var actual = s.numRollsToTarget(3,4, 9);
        assertEquals(10, actual);
    }

    @Test
    public void testCase9() {
        var s = new Solution();
        var actual = s.numRollsToTarget(3,5, 9);
        assertEquals(19, actual);
    }

    @Test
    public void testCase10() {
        var s = new Solution();
        var actual = s.numRollsToTarget(2,5, 4);
        assertEquals(3, actual);
    }



}
