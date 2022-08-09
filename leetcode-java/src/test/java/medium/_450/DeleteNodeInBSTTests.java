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
        var result = updatedRoot.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[] {5,2,6,null,4,null,7}, result);

    }

    @Test
    public void testCase2() {
        TreeNode root = TreeNode.fromArray(new Integer[]{5,3,6,2,4,null,7});;
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 0);
        var result = updatedRoot.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{5,3,6,2,4,null,7}, result );

    }

    @Test
    public void testCase3() {
        var input = new Integer[]{1,null, 2};
        TreeNode root = TreeNode.fromArray(input);

        var height = (int) (Math.log(input.length + 1)/ Math.log(2));

        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 1);
        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{2}, result);
    }
    @Test
    public void testCase4() {
        var input = new Integer[]{44,17,88,8,28,65,97,null,null,21,29,54,82,93,null};

        TreeNode root = TreeNode.fromArray(input);
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 88);

        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{44,17,82,8,28,65,97,null,null,21,29,54,null,93,null}, result);
    }

    @Test
    public void testCase5() {
        var input = new Integer[]{3,2, 4,1,null,null,null};

        TreeNode root = TreeNode.fromArray(input);
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 3);

        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{2,1, 4}, result);
    }

    @Test
    public void testCase6() {
        var input = new Integer[] {5,3,6,2,4,null,null,1};
        TreeNode root = TreeNode.fromArray(input);
        Solution solution = new Solution();
        TreeNode updatedRoot = solution.deleteNode(root, 3);

        var result = TreeNode.printTree(updatedRoot);
        Assert.assertArrayEquals(new Integer[]{5,2,6,1,4,null,null}, result);
    }






}
