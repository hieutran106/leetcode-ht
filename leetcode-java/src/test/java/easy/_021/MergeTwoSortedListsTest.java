package easy._021;

import org.junit.Assert;
import org.junit.Test;
import utils.ListNode;

public class MergeTwoSortedListsTest {
    @Test
    public void testCase1() {
        ListNode l1 = ListNode.getListFromArray(new int[]{1, 2, 4});
        ListNode l2 = ListNode.getListFromArray(new int[]{1, 3, 4});
        var result = new Solution().mergeTwoLists(l1, l2);
        Integer[] array = ListNode.getArrayFromList(result);
        Assert.assertArrayEquals(new Integer[] {1, 1, 2, 3, 4, 4}, array);
    }

    @Test
    public void testCase2() {
        ListNode l1 = ListNode.getListFromArray(new int[]{1, 2, 4});
        ListNode l2 = null;
        var result = new Solution().mergeTwoLists(l1, l2);
        Integer[] array = ListNode.getArrayFromList(result);
        Assert.assertArrayEquals(new Integer[] {1, 2, 4}, array);
    }
}
