package medium._173;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import utils.TreeNode;

public class BinarySearchTreeIteratorTest {
    @Test
    public void testCase1() {
        var input = new Integer[] {7, 3, 15, null, null, 9, 20};
        TreeNode root = TreeNode.fromArray(input);
        BSTIterator iterator = new BSTIterator(root);
        assertEquals(iterator.next(), 3);
        assertEquals(iterator.next(), 7);
        assertEquals(iterator.hasNext(), true);
        assertEquals(iterator.next(), 9);

        assertEquals(iterator.hasNext(), true); // return true
        assertEquals(iterator.next(), 15);    // return 15
        assertEquals(iterator.hasNext(), true); // return true
        assertEquals(iterator.next(), 20);    // return 20
        assertEquals(iterator.hasNext(), false); // return false
    }
}
