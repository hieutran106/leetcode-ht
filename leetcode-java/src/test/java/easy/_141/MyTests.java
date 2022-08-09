package easy._141;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class MyTests {
    @Test
    public void testExample() {
        var n0 = new ListNode(3);
        var n1 = new ListNode(2);
        var n2 = new ListNode(0);
        var n3 = new ListNode(-4);
        n0.next = n1;
        n1.next = n2;
        n2.next = n3;
        n3.next = n2;

        var solution = new Solution();
        var result = solution.hasCycle(n0);
        assertEquals(true, result);

    }

    @Test
    public void test2() {
        var n0 = new ListNode(1);
        var solution = new Solution();
        var result = solution.hasCycle(n0);
        assertEquals(false, result);
    }

}
