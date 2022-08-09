package medium._173;

import utils.TreeNode;

import java.util.Stack;


// good one
public class BSTIterator {
    private Stack<Integer> stack;
    public BSTIterator(TreeNode root) {
        this.stack = new Stack<>();
        visit(root);

    }

    private void visit(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.right != null) {
            visit(node.right);
        }
        stack.push(node.val);
        if (node.left != null) {
            visit(node.left);
        }
    }

    public int next() {
        return stack.pop();
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }
}
