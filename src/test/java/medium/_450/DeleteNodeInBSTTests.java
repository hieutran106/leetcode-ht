package medium._450;
import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

public class DeleteNodeInBSTTests {

    @Test
    public void testCase1() {
        TreeNode root = TreeNode.fromArray(new Integer[]{5,3,6,2,4,null,7});
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 3);
        var result = updatedRoot.printTree();
        Assert.assertArrayEquals(new Integer[] {5,2,6,null,4,null,7}, result);

    }

    @Test
    public void testCase2() {
        TreeNode root = TreeNode.fromArray(new Integer[]{5,3,6,2,4,null,7});;
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 0);
        var result = updatedRoot.printTree();
        Assert.assertArrayEquals(new Integer[]{5,3,6,2,4,null,7}, result );

    }

    @Test
    public void testCase3() {
        TreeNode root = TreeNode.fromArray(new Integer[]{1,null, 2});
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 1);
        var result = updatedRoot.printTree();
        Assert.assertArrayEquals(new Integer[]{2}, result);
    }


}
