package medium._230;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

public class KthSmallestElementTest {
    @Test()
    public void testCase1() {
        var input = new Integer[] {3,1,4,null,2, null, null};
        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var result = solution.kthSmallest(root, 1);
        Assert.assertEquals(1, result);
    }
    @Test()
    public void testCase2() {
        var input = new Integer[] {3,1,4,null,2, null, null};
        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var result = solution.kthSmallest(root, 3);
        Assert.assertEquals(3, result);
    }
}
