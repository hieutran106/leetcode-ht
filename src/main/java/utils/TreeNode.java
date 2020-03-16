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

    public Integer[] printTree() {
        ArrayList<Integer> list = new ArrayList();
        LinkedList<TreeNode> q = new LinkedList<>();
        q.add(this);
        while(!q.isEmpty()) {
            TreeNode node = q.poll();

            if (node != null) {
                list.add(node.val);
                if (node.left!=null || node.right !=null) {
                    q.add(node.left);
                    q.add(node.right);
                }

            } else {
                list.add(null);
            }
        }
        return list.toArray(new Integer[list.size()]);

    }

}
