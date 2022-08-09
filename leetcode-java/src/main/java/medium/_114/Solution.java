package medium._114;

import utils.TreeNode;

public class Solution {
    public void flatten(TreeNode root) {
        process(root, null);
    }

    private TreeNode process(TreeNode node, TreeNode next) {
        if (node == null) {
            return next;
        }
        var flattenedRight = process(node.right, next);
        var flattenedLeft = process(node.left, flattenedRight);
        node.right = flattenedLeft;
        node.left = null;

        return node;
    }
}
