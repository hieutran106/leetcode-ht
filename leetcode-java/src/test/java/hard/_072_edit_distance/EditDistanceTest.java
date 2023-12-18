package hard._072_edit_distance;


import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class EditDistanceTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.minDistance("horse", "ros");
        assertEquals(3, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.minDistance("intention", "execution");
        assertEquals(5, actual);
    }
}
