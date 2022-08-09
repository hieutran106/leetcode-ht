package easy._110;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class BalancedBinaryTreeTests {
    @Test
    public void testCase1() {
        var input = new Integer[]{3,2, 4,1,null,null,null};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var result = solution.isBalanced(root);
        Assert.assertEquals(true, result);
    }

    @Test
    public void testCase2() {
        var input = new Integer[] {1,2,2,3,3,null,null,4,4};
        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        var result = solution.isBalanced(root);
        Assert.assertEquals(result, false);
    }

    @Test
    public void testCase3() {
        var input = new Integer[] {1,2,2,3,3,null,null,4,4};
        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution2();
        var result = solution.isBalanced(root);
        Assert.assertEquals(result, false);
    }
}
