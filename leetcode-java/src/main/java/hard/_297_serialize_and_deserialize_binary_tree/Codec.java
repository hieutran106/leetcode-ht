package hard._297_serialize_and_deserialize_binary_tree;

import utils.TreeNode;

import java.util.*;
import java.util.stream.Collectors;


public class Codec {
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
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

        String stringResult = list.stream().map(x -> x== null? "null": x.toString()).collect(Collectors.joining(","));
        return stringResult;
    }

    public TreeNode deserialize(String dataInput) {
        if (dataInput.equals("")) {
            return null;
        }
        String[] tokens = dataInput.split(",");
        Integer[] data = new Integer[tokens.length];
        for (int i =0; i < tokens.length;i++) {
            if (tokens[i].equals("null")) {
                continue;
            }
            data[i] = new Integer(Integer.valueOf(tokens[i]));
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


