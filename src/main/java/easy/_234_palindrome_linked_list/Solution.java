package easy._234_palindrome_linked_list;

import utils.ListNode;
import utils.TreeNode;

import java.util.List;

public class Solution {
    public boolean isPalindrome(ListNode head) {
        var original = clone(head);
        ListNode tail = reverseRecursively(head);
        while (original != null) {
            if (original.val != tail.val) {
                return false;
            }
            original = original.next;
            tail = tail.next;
        }
        return true;
    }

    public ListNode clone(ListNode node) {
        if (node == null) {
            return null;
        }
        ListNode clone = new ListNode(node.val);
        clone.next = clone(node.next);
        return clone;
    }
    /**
     * Reverse the list starting from head, and return the new head node
     * @param node
     * @return the new head node
     */
    public ListNode reverseRecursively(ListNode node) {
        if (node == null) {
            return null;
        }
        if (node.next == null) {
            return node;
        }

        var last = reverseRecursively(node.next);
        // reassign
        node.next.next = node;
        node.next = null;
        return last;
    }
    

}
