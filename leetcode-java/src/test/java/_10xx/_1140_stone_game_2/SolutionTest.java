package _10xx._1140_stone_game_2;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SolutionTest {
    private Solution s;

    @BeforeEach
    public void setUp() {
        s = new Solution();
    }

    @Test
    public void testCase1() {
        var actual = s.stoneGameII(new int[]{2,7,9,4,4});
        Assertions.assertEquals(10, actual);
    }

    @Test
    public void testCase2() {
        var actual = s.stoneGameII(new int[]{1,2,3,4,5,100});
        Assertions.assertEquals(104, actual);
    }
}
    