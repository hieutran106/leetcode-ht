package medium._213_house_robber_2;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class HouseRobber2Test {

    @Test
    public void rob() {
        var s = new Solution();
        var actual = s.rob(new int[]{2, 3, 2});
        assertEquals(3, actual);
    }

    @Test
    public void rob2() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 2, 3, 1});
        assertEquals(4, actual);
    }

    @Test
    public void rob3() {
        var s = new Solution();
        var actual = s.rob(new int[]{});
        assertEquals(0, actual);
    }

    @Test
    public void rob4() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 2});
        assertEquals(2, actual);
    }

    @Test
    public void rob5() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 4, 5});
        assertEquals(5, actual);
    }

    @Test
    public void rob6() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 2, 1, 1});
        assertEquals(3, actual);
    }

    @Test
    public void unitTest1() {
        var s = new Solution();
        var unit = s.robRange(new int[]{1, 2, 1, 1}, 0, 2);
        assertEquals(2, unit);

        unit = s.robRange(new int[]{1, 2}, 0, 1);
        assertEquals(1, unit);

        unit = s.robRange(new int[]{1, 2}, 1, 2);
        assertEquals(2, unit);

        unit = s.robRange(new int[]{1, 2, 3, 1}, 0, 3);
        assertEquals(4, unit);

        unit = s.robRange(new int[]{1, 2, 3, 1}, 1, 4);
        assertEquals(3, unit);

    }
}