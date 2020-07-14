package medium._735;

import org.junit.Assert;
import org.junit.Test;

public class AsteroidCollisionTest {

    @Test
    public void testCase1() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{5, 10, -5});
        Assert.assertArrayEquals(new int[] {5, 10}, result);
    }

    @Test
    public void testCase2() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{8, -8});
        Assert.assertArrayEquals(new int[] {}, result);
    }

    @Test
    public void testCase3() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{10,2 , -5});
        Assert.assertArrayEquals(new int[] {10}, result);
    }

    @Test
    public void testCase4() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{-2, -1, 1, 2});
        Assert.assertArrayEquals(new int[] {-2, -1, 1, 2}, result);
    }

    @Test
    public void testCase5() {
        var solution = new Solution();
        var result = solution.asteroidCollision(new int[]{-2, -1, 1, 2, -10});
        Assert.assertArrayEquals(new int[] {-2, -1, -10 }, result);
    }

    @Test
    public void testCase6() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{-2, 2, -1, -2});
        Assert.assertArrayEquals(new int[] {-2 }, result);
    }
}
