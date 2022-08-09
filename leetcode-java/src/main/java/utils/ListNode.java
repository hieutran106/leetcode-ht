package utils;

import java.util.ArrayList;
import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
    }
    public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    public static ListNode getListFromArray(int[] arr) {
        if (arr.length ==0) {
            return null;
        }
        ListNode head = new ListNode(arr[0]);
        ListNode last = head;
        if (arr.length > 1) {
            for (int i =1; i < arr.length;i ++) {
                ListNode n = new ListNode(arr[i]);
                last.next = n;
                last = n;
            }
        }


        return head;
    }

    public static Integer[] getArrayFromList(ListNode head) {
        ArrayList<Integer> list = new ArrayList<>();
        while (head != null) {
            list.add(head.val);
            head = head.next;
        }
        Integer[] result = new Integer[list.size()];
        return list.toArray(result);
    }
}
