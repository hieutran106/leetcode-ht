package medium._450;


import utils.TreeNode;

import java.security.Key;

class NodePair {
    TreeNode current;
    TreeNode parent;
    public  NodePair(TreeNode current, TreeNode parent) {
        this.current = current;
        this.parent = parent;
    }
}
public class Solution {

    private TreeNode deleteLeafNode(TreeNode current, TreeNode parent, int key) {
        if (parent == null) {
            return null;
        }
        if (parent.val > key) {
            parent.left = null;
        } else {
            parent.right = null;
        }
        return parent;
    }

    private TreeNode deleteNodeWithOneChild(TreeNode current, TreeNode parent, int key, boolean hasLeftChild) {
        var grandChild = hasLeftChild ? current.left : current.right;
        if (parent == null) {
            return grandChild;
        }

        if (parent.val > key) {
            parent.left = grandChild;
        } else {
            parent.right = grandChild;
        }
        return null;

    }

    public TreeNode deleteNode(TreeNode root, int key) {
        NodePair pair = findNode(root, null, key);


        if (pair == null) {
            // not found
            return root;
        }

        // found
        var current = pair.current;
        var parent = pair.parent;



        // node to be deleted is leaf
        if (current.left == null && current.right == null) {
            var result = deleteLeafNode(current, parent, key);
            return result == null ? null : root;
        }


        // node to be deleted has only one child
        if (current.left != null && current.right == null) {
            var result = deleteNodeWithOneChild(current, parent,key,true);
            return result ==null ? root: result;
        }
        if (current.left == null && current.right != null) {
            var result = deleteNodeWithOneChild(current, parent,key,false);
            return result ==null ? root: result;
        }

        // node to be deleted has two children
        if (current.left !=null && current.right != null) {
            var inorderPair = findInorderSuccessor(current.left, null);
            var inorderCurr = inorderPair.current;
            var inorderParent = inorderPair.parent;

            // what do we do ?
            if (inorderParent == null) {
                parent.left = null;
            } else {
                // swap value
                current.val = inorderCurr.val;
                // cut grandchild
                inorderParent.right = null;
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
