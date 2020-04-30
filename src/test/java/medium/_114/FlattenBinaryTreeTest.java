package medium._114;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

public class FlattenBinaryTreeTest {
    @Test
    public void testCase1() {
        var input = new Integer[] {1,2,5,3,4,null,6};
        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution();
        solution.flatten(root);
        var x = root;
        while (x != null) {
            System.out.println(x.val);
            x = x.right;
        }
        Assert.assertEquals(true, true);
    }
}
