package medium._230;

import utils.TreeNode;

public class Solution {
    private int current = 1;
    public int kthSmallest(TreeNode root, int k) {
        return visit(root, k);
    }

    private int visit(TreeNode node, int k) {
        if (node == null) {
            return -1;
        }

        if (node.left != null) {
            var left =  visit(node.left, k);
            if (left != -1) {
                return left;
            }
        }


        if (current == k) {
            return node.val;
        }
        current +=1 ;

        if (node.right !=null) {
            var right = visit(node.right, k);
            if (right != -1) {
                return right;
            }
        }
        return -1;

    }
}
