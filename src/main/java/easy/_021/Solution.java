package easy._021;

import utils.ListNode;

public class Solution {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode tail = null;

        while (l1 != null || l2 != null) {
            ListNode appendix = null;
            if (l1 !=null && l2 == null) {
                appendix = new ListNode(l1.val);
                l1 = l1.next;
            } else if (l1 == null && l2 != null) {
                appendix = new ListNode(l2.val);
                l2 = l2.next;
            } else {
                var min = l1.val < l2.val ? l1 : l2;
                appendix = new ListNode(min.val);
                if (l1.val < l2.val) {
                    l1 = l1.next;
                } else l2 = l2.next;
            }

            if (head == null) {
                head = appendix;
                tail = head;

            } else {
                tail.next = appendix;
                tail = tail.next;
            }

        }
        return head;
    }

    public ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode tail = null;



        while (l1 != null || l2 != null) {
            ListNode appendix = null;
            if (l1 !=null && l2 == null) {
                appendix = new ListNode(l1.val);
                l1 = l1.next;
            } else if (l1 == null && l2 != null) {
                appendix = new ListNode(l2.val);
                l2 = l2.next;
            } else {
                var min = l1.val < l2.val ? l1 : l2;
                appendix = new ListNode(min.val);
                if (l1.val < l2.val) {
                    l1 = l1.next;
                } else l2 = l2.next;
            }

            if (tail != null) {
                tail.next = appendix;

            } else {
                head = appendix;
                tail =appendix;
            }

        }
        return head;
    }
}
