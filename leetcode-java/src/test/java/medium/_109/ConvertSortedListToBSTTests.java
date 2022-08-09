package medium._109;


import org.junit.Assert;
import org.junit.Test;
import utils.ListNode;
import utils.TreeNode;

public class ConvertSortedListToBSTTests {
    @Test
    public void testCase1() {
        ListNode head = ListNode.getListFromArray(new int[]{-10, -3, 0, 5, 9});
        var solution = new Solution();
        var root = solution.sortedListToBST(head);
        var result = TreeNode.printTree(root);
        Assert.assertArrayEquals(new Integer[]{0, -3, 9, -10, null, 5, null}, result);
    }
}
