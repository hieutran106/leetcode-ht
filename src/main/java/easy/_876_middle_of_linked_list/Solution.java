package easy._876_middle_of_linked_list;

import utils.ListNode;

public class Solution {
    public ListNode middleNode(ListNode head) {
        var slow = head;
        var fast = head;
        while (fast!= null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}
