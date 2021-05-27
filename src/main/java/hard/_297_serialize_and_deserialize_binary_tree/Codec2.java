package hard._297_serialize_and_deserialize_binary_tree;

import utils.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Codec2 {
    public Integer[] serialize(TreeNode root) {
        if (root == null) {
            return new Integer[]{};
        }
        ArrayList<Integer> list = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode currNode = q.remove();
            if (currNode == null) {
                list.add(null);
            } else {
                list.add(currNode.val);
                q.add(currNode.left);
                q.add(currNode.right);
            }
        }

        // remove trailing null
        while (list.get(list.size()-1) == null) {
            list.remove(list.size()-1);
        }
        Integer[] result = new Integer[list.size()];
        return list.toArray(result);
    }

    public TreeNode deserialize(Integer[] data) {
        if (data.length ==0) {
            return null;
        }
        Queue<Integer> queue = new LinkedList<>(Arrays.asList(data));
        Queue<TreeNode> treeQueue = new LinkedList<>();
        TreeNode root = new TreeNode(queue.remove().intValue());

        treeQueue.add(root);
        while (!treeQueue.isEmpty()) {
            TreeNode parent = treeQueue.remove();

            Integer left = queue.poll();
            if (left != null) {
                TreeNode leftNode = new TreeNode(left.intValue());
                parent.left = leftNode;
                treeQueue.add(leftNode);
            }
            Integer right = queue.poll();
            if (right != null) {
                TreeNode rightNode = new TreeNode(right.intValue());
                parent.right = rightNode;
                treeQueue.add(rightNode);
            }
        }
        return root;
    }
}