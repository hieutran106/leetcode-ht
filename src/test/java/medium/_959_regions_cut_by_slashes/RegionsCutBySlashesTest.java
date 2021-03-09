package medium._959_regions_cut_by_slashes;


import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class RegionsCutBySlashesTest {

    @Test
    public void testCase1() {
        var s = new Solution();
        var input = new String[]{" /", "/ "};
        var actual = s.regionsBySlashes(input);
        Assert.assertEquals(2, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var input = new String[]{"\\\\", " \\"};
        var actual = s.regionsBySlashes(input);
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var input = new String[]{"\\\\", "\\\\"};
        var actual = s.regionsBySlashes(input);
        Assert.assertEquals(4, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var input = new String[]{"//", "/ "};
        var actual = s.regionsBySlashes(input);
        Assert.assertEquals(3, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var input = new String[]{"/\\", "\\/"};
        var actual = s.regionsBySlashes(input);
        Assert.assertEquals(5, actual);
    }
}