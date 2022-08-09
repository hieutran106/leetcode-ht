package medium._337_house_robber_3;

import utils.TreeNode;

public class Solution {
    public int rob(TreeNode root) {
        var dp = dp(root);
        var rob_root = dp[0];
        var not_rob = dp[1];
        return Math.max(rob_root, not_rob);
    }

    public int[] dp(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0};
        }
        var result = new int[2];

        var left = dp(node.left);
        var right = dp(node.right);

        // rob at current => not rob at either left or right
        result[0] = node.val + left[1] + right[1];
        // not rob at current
        result[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return result;
    }

}
