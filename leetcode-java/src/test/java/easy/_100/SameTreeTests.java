package easy._100;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SameTreeTests {
    @Test
    public void testCase1() {
        // build tree
        var p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(3);

        var q = new TreeNode(1);
        q.left = new TreeNode(2);
        q.right = new TreeNode(3);
        var solution = new SameTree();
        var result = solution.isSameTree(p, q);
        assertEquals(true, result);
    }

    @Test
    public void testCase2() {
        // build tree
        var p = new TreeNode(1);
        p.left = new TreeNode(2);

        var q = new TreeNode(1);
        q.right = new TreeNode(2);

        var solution = new SameTree();
        var result = solution.isSameTree(p, q);
        assertEquals(false, result);

    }

    @Test
    public void testCase3() {
        // build tree
        var p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(1);

        var q = new TreeNode(1);
        q.left = new TreeNode(1);
        q.right = new TreeNode(2);
        var solution = new SameTree();
        var result = solution.isSameTree(p, q);
        assertEquals(false, result);
    }
    @Test
    public void testCase4() {
        // build tree
        TreeNode p = null;
        TreeNode q = null;
        var solution = new SameTree();
        var result = solution.isSameTree(p, q);
        assertEquals(true, result);
    }

    @Test
    public void testCase5() {
        var p = new TreeNode(1);
        p.left = null;
        p.right = new TreeNode(2);
        p.right.left = new TreeNode(3);


        var q = new TreeNode(1);
        q.left = null;
        q.right = new TreeNode(2);
        q.right.left = null;
        q.right.right = new TreeNode(3);

        var solution = new SameTree();
        var result = solution.isSameTree(p, q);
        assertEquals(false, result);
    }
}
