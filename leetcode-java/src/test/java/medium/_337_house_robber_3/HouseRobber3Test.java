package medium._337_house_robber_3;

import org.junit.jupiter.api.Test;
import utils.TreeNode;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HouseRobber3Test {

    @Test
    public void testCase1() {
        var s = new Solution();
        var intput = TreeNode.fromArray(new Integer[]{3, 2, 3, null, 3, null, 1});
        var actual = s.rob(intput);
        assertEquals(7, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var intput = TreeNode.fromArray(new Integer[]{3,4,5,1,3,null,1});
        var actual = s.rob(intput);
        assertEquals(9, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var intput = TreeNode.fromArray(new Integer[]{1, 2, null});
        var actual = s.rob(intput);
        assertEquals(2, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var intput = TreeNode.fromArray(new Integer[]{1, 2, 3});
        var actual = s.rob(intput);
        assertEquals(5, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        TreeNode input = null;
        var actual = s.rob(input);
        assertEquals(0, actual);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        var intput = TreeNode.fromArray(new Integer[]{1, null, 2});
        var actual = s.rob(intput);
        assertEquals(2, actual);
    }


}