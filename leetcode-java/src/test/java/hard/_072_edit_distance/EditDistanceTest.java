package hard._072_edit_distance;


import org.junit.Assert;
import org.junit.Test;

public class EditDistanceTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.minDistance("horse", "ros");
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.minDistance("intention", "execution");
        Assert.assertEquals(5, actual);
    }
}
