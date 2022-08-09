package easy._206_reverse_linked_list;

import utils.ListNode;

public class Solution {
    public ListNode reverseList(ListNode node) {
        if (node == null) {
            return null;
        }
        if (node.next == null) {
            return node;
        }

        var last = reverseList(node.next);
        // reassign
        node.next.next = node;
        node.next = null;
        return last;
    }
}
