package easy._876_middle_of_linked_list;

import org.junit.jupiter.api.Test;
import utils.ListNode;
import org.junit.jupiter.api.Assertions;

public class MiddleOfLinkedListTest {
    @Test
    public void testCase1() {
        var head = ListNode.getListFromArray(new int[]{1, 2, 3, 4, 5});
        var s = new Solution();
        var actual = s.middleNode(head);
        Assertions.assertEquals(actual.val, 3);

    }

    @Test
    public void testCase2() {
        var head = ListNode.getListFromArray(new int[]{1, 2});
        var s = new Solution();
        var actual = s.middleNode(head);
        Assertions.assertEquals(actual.val, 2);
    }

    @Test
    public void testCase3() {
        var head = ListNode.getListFromArray(new int[]{1, 2, 3});
        var s = new Solution();
        var actual = s.middleNode(head);
        Assertions.assertEquals(actual.val, 2);
    }
}
