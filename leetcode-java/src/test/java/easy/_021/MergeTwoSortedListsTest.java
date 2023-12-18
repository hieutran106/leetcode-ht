package easy._021;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;
import utils.ListNode;

public class MergeTwoSortedListsTest {
    @Test
    public void testCase1() {
        ListNode l1 = ListNode.getListFromArray(new int[]{1, 2, 4});
        ListNode l2 = ListNode.getListFromArray(new int[]{1, 3, 4});
        var result = new Solution().mergeTwoLists(l1, l2);
        Integer[] array = ListNode.getArrayFromList(result);
        assertArrayEquals(new Integer[] {1, 1, 2, 3, 4, 4}, array);
    }

    @Test
    public void testCase2() {
        ListNode l1 = ListNode.getListFromArray(new int[]{1, 2, 4});
        ListNode l2 = null;
        var result = new Solution().mergeTwoLists(l1, l2);
        Integer[] array = ListNode.getArrayFromList(result);
        assertArrayEquals(new Integer[] {1, 2, 4}, array);
    }
}
