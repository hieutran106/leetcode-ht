package utils;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ConcurrentLinkedDeque;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) {
        val = x;
    }
    public TreeNode(int x, TreeNode left, TreeNode right) {
        val  =x;
        this.left = left;
        this.right = right;
    }

    public static TreeNode fromArray(Integer[] input) {
        int height = (int)(Math.log(input.length) / Math.log(2));
        int length = (int)Math.pow(2, height) -1;
        TreeNode[]  nodes = new TreeNode[input.length];
        for (int i = input.length -1; i >= 0; i--) {
            if (input[i] == null) {
                continue;
            }
            nodes[i] = new TreeNode(input[i]);
            int leftIndex = 2 *i +1;
            if (leftIndex < input.length) {
                nodes[i].left = nodes[leftIndex];
            }

            int rightIndex = 2 * i + 2;
            if (rightIndex < input.length) {
                nodes[i].right = nodes[rightIndex];
            }
        }
        return nodes[0];
    }


    public static int findHeight(TreeNode root) {
        return TreeNode.dig(root, 0);

    }

    private static int dig(TreeNode node, int height) {
        if (node == null) {
            return height;
        }
        int left = TreeNode.dig(node.left, height + 1);
        int right = TreeNode.dig(node.right, height + 1);
        return Math.max(left, right);
    }

    public static Integer[] printTree(TreeNode root) {
        if (root == null) {
            return new Integer[]{};
        }

        int height = TreeNode.findHeight(root);
        ArrayList<TreeNode> parent = new ArrayList<TreeNode>();
        parent.add(root);
        ArrayList<TreeNode> children = new ArrayList<TreeNode>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int h = 1; h <= height; h++) {
            for (var node : parent) {
                if (h < height) {
                    if (node == null) {
                        children.add(null);
                        children.add(null);
                    } else {
                        children.add(node.left);
                        children.add(node.right);
                    }

                }
                result.add(node == null ? null : node.val);
            }
            parent = children;
            children = new ArrayList<TreeNode>();
        }
        return result.toArray(new Integer[result.size()]);

    }


    public static Integer[] serialize(TreeNode root) {
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

    public static TreeNode deserialize(Integer[] data) {
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
