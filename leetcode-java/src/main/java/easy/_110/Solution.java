package easy._110;

import utils.TreeNode;

public class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        var lHeight  = getHeight(root.left, 0);
        var rHeight = getHeight(root.right, 0);

        if (Math.abs(lHeight - rHeight) > 1) {
            return false;
        }

        return isBalanced(root.left) && isBalanced(root.right);

    }

    private int getHeight(TreeNode root, int h) {
        if (root == null) {
            return h;
        }
        return Math.max(getHeight(root.left, h +1), getHeight(root.right, h +1));
    }
}

class Solution2 {
    public boolean isBalanced(TreeNode root) {
        return  dfsHeight(root) != -1;
    }

    private int dfsHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftHeight = dfsHeight(root.left);
        if (leftHeight == -1) {
            return -1;
        }
        int rightHeight =  dfsHeight(root.right);
        if (rightHeight == -1) {
            return -1;
        }

        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
