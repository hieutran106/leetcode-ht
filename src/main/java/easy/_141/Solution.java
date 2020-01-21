package easy._141;


import java.util.HashSet;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}
public class Solution {

    HashSet<ListNode> set = new HashSet<>();
    public boolean hasCycle1(ListNode head) {
        var walk = head;
        while (walk != null) {
            if (set.contains(walk)) {
                return true;
            }

            set.add(walk);
            walk = walk.next;
        }

        return false;
    }

    // implement Floyd's cycle-finding algorithm
    // use two pointer, walker and runner
    // walker move one step at a time
    // runner move two step at a time
    //
    public boolean hasCycle(ListNode head) {
        if(head==null) return false;

        var walker = head;
        var runner = head;



        while (runner.next != null && runner.next.next != null) {
            walker = walker.next;
            runner = runner.next.next;
            if (walker == runner) {
                return true;
            }

        }
        return false;
    }

}
