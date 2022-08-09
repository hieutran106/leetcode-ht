package medium._113;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }
}
public class PathSumTwo {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> paths = new ArrayList<>();
        traverse(root, paths, new int[1000], 0);

        var result = paths.stream().filter(x -> {
            Integer s = x.stream().reduce(0, (a, b) -> a + b);
            return s == sum;
        }).collect(Collectors.toList());

        return result;
    }

    private void traverse(TreeNode node, List<List<Integer>> paths, int[] path, int len) {
        if (node == null) {
            return;
        }

        path[len] = node.val;
        len ++;
        if (node.left == null && node.right == null) {
            paths.add(pathFor(path, len));
            return;
        }
        traverse(node.left, paths, path, len);
        traverse(node.right, paths, path, len);

    }

    private List<Integer> pathFor(int[] path, int len) {
        List<Integer> result = new ArrayList<>(len);
        for (int i =0; i < len; i ++) {
            result.add(path[i]);
        }
        return result;
    }

}
