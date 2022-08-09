package easy._538;

import utils.TreeNode;

import javax.swing.*;

public class Solution {
    public TreeNode convertBST(TreeNode root) {
        helper(root, 0);
        return root;
    }

    public int inorder(TreeNode node, int value) {
       if (node == null) {
           return 0;
       }
       int rightAmount = 0;
       if (node.right != null) {
           rightAmount = inorder(node.right, value);
       }
       int old = node.val;
       node.val += rightAmount + value;

        int leftAmount = 0;
       if (node.left != null) {
            leftAmount = inorder(node.left, node.val);
       }
       return rightAmount + old + leftAmount;
    }

    private int helper(TreeNode node, int sum) {
        if (node == null) {
            return sum;
        }
        sum = helper(node.right, sum);
        node.val += sum;
        return helper(node.left, node.val);
    }
}
