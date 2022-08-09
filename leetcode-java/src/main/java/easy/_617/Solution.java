package easy._617;

import utils.TreeNode;

public class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        TreeNode root = helper(t1, t2);
        return root;
    }
    public TreeNode helper(TreeNode n1, TreeNode n2) {
        if (n1 == null && n2 == null) {
            return null;
        } else if (n1 ==null && n2 != null) {
            var n = new TreeNode(n2.val);
            n.left = helper(null, n2.left);
            n.right = helper(null, n2.right);
            return n;
        } else if (n1 != null && n2 == null) {
            var n = new TreeNode(n1.val);
            n.left = helper(n1.left, null);
            n.right = helper(n1.right, null);
            return n;
        } else {
            var n = new TreeNode(n1.val + n2.val);
            n.left = helper(n1.left, n2.left);
            n.right = helper(n1.right, n2.right);
            return n;
        }
    }
}
