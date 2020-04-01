package easy._452;

import utils.Node;

import java.util.ArrayList;
import java.util.List;



public class Solution {
    public List<Integer> preorder(Node root) {
         List<Integer> result = new ArrayList<>();
         helper(root, result);
         return result;
    }
    private void helper(Node root, List<Integer> result) {
        if (root == null) {
            return;
        }
        result.add(root.val);
        for (var child : root.children) {
            helper(child, result);
        }
    }
}
