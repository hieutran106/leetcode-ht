package easy._101;

import utils.TreeNode;


public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        int height = getHeight(root, 0);
        int length = (int)(Math.pow(2, height)) -1;
        TreeNode[] nodeArray = new TreeNode[length];
        nodeArray[0] = root;
        for (int i =1; i < nodeArray.length; i++) {
            int parentIndex = (int) (i -1) /2;
            if (i %2 ==0) {
                nodeArray[i] = nodeArray[parentIndex] != null ? nodeArray[parentIndex].right : null;
            } else {
                nodeArray[i] = nodeArray[parentIndex] != null ? nodeArray[parentIndex].left : null;
            }
        }

        Integer[] values = new Integer[length];
        for (int i =0; i < nodeArray.length; i++) {
            if  (nodeArray[i] != null) {
                values[i] = nodeArray[i].val;
            }
        }

        for (int i = 1; i < height; i ++) {
            int start = (int) Math.pow(2, i ) -1;
            int end = (int) Math.pow(2,i + 1) - 1;
            var check = isPalindrome(values, start, end);
            if (!check) {
                return false;
            }

        }
        return true;


    }
    private boolean isPalindrome(Integer[] array, int start, int end) {
        boolean result = true;
        int j = start;
        int k = end -1;
        while (j < k) {
            if (array[j] != null & array[k] == null) {
                return false;
            } else if (array[j] == null && array[k] != null) {
                return false;
            } else if (array[j] != null && array[k] != null) {
                if (array[j].intValue() != array[k].intValue()) return false;
            }
            j ++;
            k--;
        }
        return result;

    }
    private int getHeight(TreeNode root, int height) {
        if (root == null) {
            return 0;
        }
        return Math.max(getHeight(root.left, height), getHeight(root.right, height)) +1;
    }
}

class Solution2 {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirror(root.left, root.right);

    }
    private boolean isMirror(TreeNode tree1, TreeNode tree2) {
        if (tree1 == null && tree2 == null) {
            return true;
        }
       if (tree1 ==null || tree2==null) {
           return false;
       }
       if (tree1.val != tree2.val) {
           return false;
       }


       return isMirror(tree1.left, tree2.right) && isMirror(tree1.right, tree2.left);
    }
}