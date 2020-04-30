package medium._173;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

public class BinarySearchTreeIteratorTest {
    @Test
    public void testCase1() {
        var input = new Integer[] {7, 3, 15, null, null, 9, 20};
        TreeNode root = TreeNode.fromArray(input);
        BSTIterator iterator = new BSTIterator(root);
        Assert.assertEquals(iterator.next(), 3);
        Assert.assertEquals(iterator.next(), 7);
        Assert.assertEquals(iterator.hasNext(), true);
        Assert.assertEquals(iterator.next(), 9);

        Assert.assertEquals(iterator.hasNext(), true); // return true
        Assert.assertEquals(iterator.next(), 15);    // return 15
        Assert.assertEquals(iterator.hasNext(), true); // return true
        Assert.assertEquals(iterator.next(), 20);    // return 20
        Assert.assertEquals(iterator.hasNext(), false); // return false
    }
}
