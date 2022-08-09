package easy._538;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
public class TestConvertToGreaterTree {

    @Test
    public void testCase1() {
        var input = new Integer[]{5, 2, 13};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var updatedRoot = solution.convertBST(root);
        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{18, 20 ,13}, result);

    }

    @Test
    public void testCase2() {
        var input = new Integer[]{2,0,3,-4,1};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var updatedRoot = solution.convertBST(root);
        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{5,6,3,2,6, null, null}, result);

    }

    @Test
    public void testCase3() {
        var input = new Integer[]{0,-1,2,-3,null,null,4};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var updatedRoot = solution.convertBST(root);
        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{6,5,6,2,null,null,4}, result);

    }
}
