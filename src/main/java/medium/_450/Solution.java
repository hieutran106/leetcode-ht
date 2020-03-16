package medium._450;


import utils.TreeNode;

class NodePair {
    TreeNode current;
    TreeNode parent;
    public  NodePair(TreeNode current, TreeNode parent) {
        this.current = current;
        this.parent = parent;
    }
}
public class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        NodePair pair = findNode(root, null, key);
        if (pair == null) {
            // not found
            return root;
        }

        var current = pair.current;
        var parent = pair.parent;

        // node to be deleted is leaf
        if (current.left == null && current.right == null) {
            if (parent == null) {
                return null;
            }
            if (parent.val > key) {
                parent.left = null;
            } else {
                parent.right = null;
            }
        }

        // node to be deleted has only one child
        if (current.left != null && current.right == null) {
            if (parent.val > key) {
                // left left child tree
                parent.left = current.left;
            } else {
                parent.right = current.left;
            }
        }
        if (current.left == null && current.right != null) {

            if (parent.val > key) {
                parent.left = current.right;
            } else {
                parent.right = current.right;
            }

        }

        // node to be deleted has two children
        if (current.left !=null && current.right != null) {
            var inorder = findInorderSuccessor(current.left, null);
            var r = inorder.current;
            var rParent = inorder.parent;

            current.val = r.val;

            if (rParent == null) {
                current.left = null;
            } else {
                rParent.right = r.left;
            }


        }


        return root;
    }

    private NodePair findInorderSuccessor(TreeNode current, TreeNode parent) {
        if (current.right != null) {
            return findInorderSuccessor(current.right, current);
        }
        return new NodePair(current, parent);
    }



    private NodePair findNode(TreeNode current, TreeNode parent, int key) {
        if (current ==null) {
            return null;
        }
        if (current.val == key) {
            return new NodePair(current, parent);
        }
        if (key > current.val) {
            return findNode(current.right, current, key);
        } else {
            return findNode(current.left, current, key);
        }

    }
}
