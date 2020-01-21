package medium._142;

public class Solution {

    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        var walker = head;
        var runner = head;

        while (runner.next != null && runner.next.next !=null) {
            walker = walker.next;
            runner = runner.next.next;

            if (walker == runner) {
               // use another seeker from head to detect
                // because walker need to walk y more nodes (y-th is position of where the circle start
                var seeker = head;
                while ( seeker != walker) {
                    walker = walker.next;
                    seeker = seeker.next;
                }
                return walker;
            }
        }
        return null;
    }
}

class ListNode {
    int val;
    ListNode next;
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}
