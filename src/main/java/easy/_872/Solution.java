package easy._872;

import utils.TreeNode;

import java.util.ArrayList;

public class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> leaf1 = new ArrayList<>();
        ArrayList<Integer> leaf2 = new ArrayList<>();
        getLeaves(root1, leaf1);
        getLeaves(root2, leaf2);

        return leaf1.equals(leaf2);
    }
    private void getLeaves(TreeNode node, ArrayList<Integer> array) {
        if (node.right == null && node.left == null) {
            array.add(node.val);
        }
        if (node.right != null) {
            getLeaves(node.right, array);
        }
        if (node.left != null) {
            getLeaves(node.left, array);
        }

    }
}
