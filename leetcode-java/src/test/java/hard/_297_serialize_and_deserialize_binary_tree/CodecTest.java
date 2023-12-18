package hard._297_serialize_and_deserialize_binary_tree;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import utils.TreeNode;

import java.util.Arrays;


public class CodecTest {

    @Test
    public void testCase1() {
        TreeNode root = TreeNode.fromArray(new Integer[]{1, 2, 3});
        var codec = new Codec2();
        Integer[] data = codec.serialize(root);
        assertArrayEquals(data, new Integer[]{1, 2, 3});
    }

    @Test
    public void testCase2() {
        TreeNode root = TreeNode.fromArray(new Integer[]{1, null, 3});
        var codec = new Codec2();
        Integer[] data = codec.serialize(root);
        assertArrayEquals(data, new Integer[]{1, null, 3});
    }

    @Test
    public void testCase3() {
        var codec = new Codec2();
        TreeNode root = codec.deserialize(new Integer[]{1, null, 2});
        Integer[] serialized_tree = codec.serialize(root);
        assertArrayEquals(serialized_tree, new Integer[]{1, null, 2});

    }

    @Test
    public void testCase4() {
        // build a tree
        TreeNode root = new TreeNode(1, new TreeNode(2), null);
        TreeNode right = new TreeNode(3, new TreeNode(4), new TreeNode(5));
        root.right = right;

        var codec = new Codec2();
        Integer[] serialized_tree = codec.serialize(root);
        System.out.println(Arrays.toString(serialized_tree));
        assertArrayEquals(serialized_tree, new Integer[]{1, 2, 3, null, null, 4, 5});

    }

    @Test
    public void testCase5() {
        var codec = new Codec2();
        TreeNode root = codec.deserialize(new Integer[]{1, null, 2, 3, null, null, 5});
        assertEquals(root.val, 1);
        assertEquals(root.right.left.val, 3);
        assertEquals(root.right.left.right.val, 5);

    }

    @Test
    public void testCase6() {
        var codec = new Codec2();
        Integer[] input = new Integer[]{1, 2, 3};
        TreeNode root = codec.deserialize(input);
        Integer[] data = codec.serialize(root);
        assertArrayEquals(data, input);
    }

    @Test
    public void testCase7() {
        var codec = new Codec2();
        Integer[] input = new Integer[]{};
        TreeNode root = codec.deserialize(input);
        Integer[] data = codec.serialize(root);
        assertArrayEquals(data, input);
    }
    @Test
    public void testCase8() {
        var codec = new Codec2();
        Integer[] input = new Integer[]{1,2,3,4, null, 5, 6, 7};
        TreeNode root = codec.deserialize(input);
        Integer[] data = codec.serialize(root);
        assertArrayEquals(data, input);
    }


    @Test
    public void testCase9() {
        var codec = new Codec();
        String input = "";
        TreeNode root = codec.deserialize(input);
        String data = codec.serialize(root);
        assertEquals(data, input);
    }

    @Test
    public void testCase10() {
        var codec = new Codec();
        String input = "1,2";
        TreeNode root = codec.deserialize(input);
        String data = codec.serialize(root);
        assertEquals(data, input);
    }




}