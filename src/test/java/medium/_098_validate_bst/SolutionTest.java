package medium._098_validate_bst;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{2, 1, 3});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, true);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{5,1,4,null,null,3,6});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{5,1,4,null,null,3,6});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{5, 2, 7, null, null, 6, 8});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, true);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{5, 2, 7, null, null, 6, 7});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, true);
    }

    @Test
    public void testCase7() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{3, 1, 5, 0, 1});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase8() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{5,4,6,null,null,3,7});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase9() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{2147483647});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, true);
    }

    @Test
    public void testCase10() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{Integer.MIN_VALUE, Integer.MIN_VALUE});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase11() {
        var s = new Solution();
        TreeNode root = TreeNode.deserialize(new Integer[]{Integer.MAX_VALUE, Integer.MAX_VALUE});
        var actual = s.isValidBST(root);
        Assert.assertEquals(actual, false);
    }
}