package easy._572;

import utils.TreeNode;

// best solution from discussion
public class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }

    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;

        if (s.val != t.val) return false;

        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}

class Solution2 {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        return helper(s, t, true);
    }

    private boolean helper(TreeNode s, TreeNode t, boolean isTop) {
        if (s == null && t == null) {
            return true;
        } else if (s == null && t != null) {
            return false;
        } else if (s != null && t == null) {
            return false;
        }

        if (s.val == t.val) {
            var left = helper(s.left, t.left, false);
            var right = helper(s.right, t.right, false);
            if (left && right) return true;
        }
        // go down
        if (isTop == false) {
            return false;
        }
        return helper(s.left, t, true) || helper(s.right, t, true);
    }
}
