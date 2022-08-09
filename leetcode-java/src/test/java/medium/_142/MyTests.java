package medium._142;



import org.junit.Assert;
import org.junit.Test;
import org.w3c.dom.NodeList;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

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
        n3.next = n1;

        var solution = new Solution();
        var result = solution.detectCycle(n0);
        System.out.println(result.val);
        assertEquals(n1, result);

    }

    @Test
    public void test2() {
        var n0 = new ListNode(1);
        var solution = new Solution();
        var result = solution.detectCycle(n0);
        assertEquals(null, result);
    }

    @Test
    public void test3() {
        var n0 = new ListNode(1);
        var n1 = new ListNode(2);

        n0.next = n1;
        n1.next = n0;

        var solution = new Solution();
        var result = solution.detectCycle(n0);
        assertEquals(n0, result);
    }

    @Test
    public void test4() {
        var input = new int[]{-1,-7,7,-4,19,6,-9,-6,-2,-5};
        var nodes = Arrays.stream(input).mapToObj(x -> new ListNode(x)).toArray();
        for (int i =0; i < nodes.length; i ++) {
            var node = (ListNode)nodes[i];
            if ( i < nodes.length -1 ) {
                node.next = (ListNode)nodes[i+1];
            }
        }
        var head = (ListNode)nodes[6];
        ((ListNode)nodes[nodes.length-1]).next = head;

        var solution = new Solution();
        var result = solution.detectCycle((ListNode)nodes[0]);
        assertEquals(head, result);
    }

    @Test
    public void test5() {
        var input = new int[]{-1,-7,7,-4,19,6,-9,-6,-2,-5};
        var nodes = Arrays.stream(input).mapToObj(x -> new ListNode(x)).toArray();
        for (int i =0; i < nodes.length; i ++) {
            var node = (ListNode)nodes[i];
            if ( i < nodes.length -1 ) {
                node.next = (ListNode)nodes[i+1];
            }
        }

        var head = (ListNode)nodes[3];
        ((ListNode)nodes[nodes.length-1]).next = head;

        var solution = new Solution();
        var result = solution.detectCycle((ListNode)nodes[0]);
        assertEquals(head, result);

    }
}
