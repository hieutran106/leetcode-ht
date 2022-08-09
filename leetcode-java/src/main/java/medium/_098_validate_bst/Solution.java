package medium._098_validate_bst;

import utils.TreeNode;

import java.util.ArrayList;

/**
 * Serialize BST(inorder traversal) into array and check if the elements in array are in strict ascending order
 */
public class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        ArrayList<Integer> list = new ArrayList<>();
        inorderTraversal(root, list);
        for (int i=1; i < list.size();i++) {
            if (list.get(i) <= list.get(i-1)) {
                return false;
            }
        }
        return true;
    }


    public void inorderTraversal(TreeNode root, ArrayList<Integer> list) {
        // Recursively traverse the left subtree
        if (root.left != null) {
            inorderTraversal(root.left, list);
        }
        // perform the visit action for position p
        list.add(root.val);
        // Recursively traverse the right subtree
        if (root.right != null) {
            inorderTraversal(root.right, list);
        }
    }

}
