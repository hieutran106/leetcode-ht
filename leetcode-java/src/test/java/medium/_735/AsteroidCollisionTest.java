package medium._735;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class AsteroidCollisionTest {

    @Test
    public void testCase1() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{5, 10, -5});
        assertArrayEquals(new int[] {5, 10}, result);
    }

    @Test
    public void testCase2() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{8, -8});
        assertArrayEquals(new int[] {}, result);
    }

    @Test
    public void testCase3() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{10,2 , -5});
        assertArrayEquals(new int[] {10}, result);
    }

    @Test
    public void testCase4() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{-2, -1, 1, 2});
        assertArrayEquals(new int[] {-2, -1, 1, 2}, result);
    }

    @Test
    public void testCase5() {
        var solution = new Solution();
        var result = solution.asteroidCollision(new int[]{-2, -1, 1, 2, -10});
        assertArrayEquals(new int[] {-2, -1, -10 }, result);
    }

    @Test
    public void testCase6() {
        var solution = new Solution2();
        var result = solution.asteroidCollision(new int[]{-2, 2, -1, -2});
        assertArrayEquals(new int[] {-2 }, result);
    }
}
