package medium._763;

import org.junit.Assert;
import org.junit.Test;

public class PartitionLabelsTest {
    public static ISolution763 getSolution() {
        return new Solution2();
    }
    @Test
    public void testCase1() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("ababcbacadefegdehijhklij");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{9,7,8});
    }

    @Test
    public void testCase2() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("hijhklij");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{8});
    }

    @Test
    public void testCase3() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("abcd");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{1, 1, 1, 1});
    }

    @Test
    public void testCase4() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("abad");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{3, 1});
    }

    @Test
    public void testCase5() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{});
    }

    @Test
    public void testCase6() {
        var s = PartitionLabelsTest.getSolution();
        var result = s.partitionLabels("aac");
        var actual = result.toArray(new Integer[result.size()]);
        Assert.assertArrayEquals(actual, new Integer[]{2,1});
    }

}
