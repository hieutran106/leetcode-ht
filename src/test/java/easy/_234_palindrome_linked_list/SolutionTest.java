package easy._234_palindrome_linked_list;

import org.junit.Assert;
import org.junit.Test;
import utils.ListNode;

import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testCase10() {

        var s = new Solution();
        var actual = s.isPalindrome(null);
        Assert.assertEquals(true, actual);
    }

    @Test
    public void testCase1() {
        var input = ListNode.getListFromArray(new int[]{1, 2});
        var s = new Solution();
        var actual = s.isPalindrome(input);
        Assert.assertEquals(false, actual);
    }

    @Test
    public void testCase2() {
        var input = ListNode.getListFromArray(new int[]{1, 2, 2, 1});
        var s = new Solution();
        var actual = s.isPalindrome(input);
        Assert.assertEquals(true, actual);
    }

    @Test
    public void testCase3() {
        var input = ListNode.getListFromArray(new int[]{1, 2, 1});
        var s = new Solution();
        var actual = s.isPalindrome(input);
        Assert.assertEquals(true, actual);
    }

    @Test
    public void testCase4() {
        var input = ListNode.getListFromArray(new int[]{1, 2, 3, 4, 2, 1});
        var s = new Solution();
        var actual = s.isPalindrome(input);
        Assert.assertEquals(false, actual);
    }

    @Test
    public void testCase5() {
        var input = ListNode.getListFromArray(new int[]{1, 2});
        var s = new Solution();
        var actual = s.reverseRecursively(input);
        Assert.assertEquals(1, 1);
    }
}