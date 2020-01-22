package easy._100;


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }

}
public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return  true;
        }
        var currentSame = isSameNode(p, q);
        if (!currentSame) {
            return false;
        }

        return isSameNode(p.left, q.left) && isSameNode(p.right, q.right);



    }
    private boolean isSameNode(TreeNode  n1, TreeNode n2) {
        if (n1 == null & n2 == null) {
            return true;
        }
        if (n1 != null && n2 != null) {
            return n1.val == n2.val;
        }
        return false;
    }
}
