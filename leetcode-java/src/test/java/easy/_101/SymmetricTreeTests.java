package easy._101;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import utils.TreeNode;

public class SymmetricTreeTests {
    @Test
    public void testCase1() {
        var input = new Integer[]{1,2,2,3,4,4,3};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution2();
        var result = solution.isSymmetric(root);
        assertEquals(result, true);
    }

    @Test
    public void testCase2() {
        var input = new Integer[]{1,2,2,null,3,null,3};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution2();
        var result = solution.isSymmetric(root);
        assertEquals(result, false);
    }

    @Test
    public void testCase3() {
        var input = new Integer[]{1};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution2();
        var result = solution.isSymmetric(root);
        assertEquals(result, true);
    }

    @Test
    public void testCase4() {
        var solution = new Solution2();
        var result = solution.isSymmetric(null);
        assertEquals(result, true);
    }

    @Test
    public void testCase5() {
        var input = new Integer[]{1,2 ,3};

        TreeNode root = TreeNode.fromArray(input);
        var solution = new Solution2();
        var result = solution.isSymmetric(root);
        assertEquals(result, false);
    }
}
