package easy._572;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import utils.TreeNode;

public class SubtreeAnotherTreeTest {
    @Test
    public void testCase1() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{3, 4, 5, 1, 2, null, null});
        TreeNode t = TreeNode.fromArray(new Integer[]{4, 1, 2});
        var actual = solution.isSubtree(s, t);
        assertEquals(true, actual);

    }

    @Test
    public void testCase2() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{3,4,5,1,2,null, null, null, null, 0, null, null, null, null, null });
        TreeNode t = TreeNode.fromArray(new Integer[]{4, 1, 2});
        var actual = solution.isSubtree(s, t);
        assertEquals(false, actual);
    }

    @Test
    public void testCase3() {
        var solution = new Solution();
        TreeNode t = TreeNode.fromArray(new Integer[]{4, 1, 2});
        var actual = solution.isSubtree(t, t);
        assertEquals(true, actual);
    }

    @Test
    public void testCase4() {
        var solution = new Solution();
        TreeNode t = TreeNode.fromArray(new Integer[]{3, 4, 5, 1, 2, null, null, 0});
        var actual = solution.isSubtree(t, t);
        assertEquals(true, actual);
    }

    @Test
    public void testCase5() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{3, 4, 5, 1, 2, null, null, 0});
        TreeNode t = TreeNode.fromArray(new Integer[]{4, 1, 2});
        var actual = solution.isSubtree(s, t);
        assertEquals(false, actual);
    }

    @Test
    public void testCase6() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{1, 1});
        TreeNode t = TreeNode.fromArray(new Integer[]{1});
        var actual = solution.isSubtree(s, t);
        assertEquals(true, actual);
    }

    @Test
    public void testCase7() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{2, 1});
        TreeNode t = TreeNode.fromArray(new Integer[]{1});
        var actual = solution.isSubtree(s, t);
        assertEquals(true, actual);
    }

    @Test
    public void testCase8() {
        var solution = new Solution();
        TreeNode s = TreeNode.fromArray(new Integer[]{3, 4, 5, 1, null, 2});
        TreeNode t = TreeNode.fromArray(new Integer[]{3, 1, 2});
        var actual = solution.isSubtree(s, t);
        assertEquals(false, actual);
    }
}
