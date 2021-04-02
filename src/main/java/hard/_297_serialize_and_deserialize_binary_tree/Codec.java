package hard._297_serialize_and_deserialize_binary_tree;

import utils.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;


public class Codec {
    public Integer[] serialize(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        serializeHelper(root, list);
        Integer[] result = new Integer[list.size()];
        return list.toArray(result);
    }


    private void serializeHelper(TreeNode node, ArrayList<Integer> list) {
        if (node == null) {
            list.add(null);
            return;
        }
        if (node.val == 3) {
            System.out.println("Inter here");
        }
        list.add(node.val);
        if (node.left == null && node.right == null) {
            return;
        }
        serializeHelper(node.left, list);
        serializeHelper(node.right, list);
    }

    public TreeNode deserialize(Integer[] data) {
        Queue<Integer> queue = new LinkedList<>(Arrays.asList(data));
        TreeNode root = deserializeHelper(queue);
        return root;
    }

    private TreeNode deserializeHelper(Queue<Integer> queue) {
        Integer head = queue.poll();
        if (head == null) {
            return null;
        }
        TreeNode node = new TreeNode(head.intValue());
        if (node.val ==2) {
            System.out.println("here");
        }
        node.left = deserializeHelper(queue);
        node.right = deserializeHelper(queue);
        return node;
    }
}
