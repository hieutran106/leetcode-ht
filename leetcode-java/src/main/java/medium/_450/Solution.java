package medium._450;


import utils.TreeNode;




public class Solution {

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return root;
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        } else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        } else { // found node to be delete
            if (root.left == null) {
                return root.right;

            } else if (root.right == null) {
                return root.left;
            }
            // node with two children, replace inOrder successor (minVal) in the right subtree
            root.val = getMax(root.left);
            root.left = deleteNode(root.left, root.val);
        }
        return root;
    }
    private int getMax(TreeNode root) {
        while (root.right != null) {root = root.right;}
        return root.val;
    }

}
