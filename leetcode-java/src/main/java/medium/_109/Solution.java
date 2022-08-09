package medium._109;

import utils.ListNode;
import utils.TreeNode;

import java.util.ArrayList;

public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        ArrayList<Integer> list = new ArrayList<>();
        while (head != null) {
            list.add(head.val);
            head = head.next;
        }
        TreeNode root = createTree(list, 0, list.size() -1);
        return root;
    }

    private TreeNode createTree(ArrayList<Integer> list, int start, int end) {
        if (end < start) {
            return null;
        }
        if (start == end) {
            return new TreeNode(list.get(start));
        }
        int mid = Math.round((start + end) / 2);
        TreeNode node = new TreeNode(list.get(mid));
        node.left = createTree(list,start, mid-1);
        node.right = createTree(list, mid +1, end);
        return  node;
    }
}
