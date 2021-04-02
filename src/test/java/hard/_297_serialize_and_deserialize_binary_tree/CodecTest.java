package hard._297_serialize_and_deserialize_binary_tree;

import org.junit.Assert;
import org.junit.Test;
import utils.TreeNode;

import static org.junit.Assert.*;

public class CodecTest {

    @Test
    public void testCase1() {
        TreeNode root = TreeNode.fromArray(new Integer[]{1, 2, 3});
        var codec = new Codec();
        Integer[] data = codec.serialize(root);
        Assert.assertArrayEquals(data, new Integer[]{1, 2, 3});
    }

    @Test
    public void testCase2() {
        TreeNode root = TreeNode.fromArray(new Integer[]{1, null, 3});
        var codec = new Codec();
        Integer[] data = codec.serialize(root);
        Assert.assertArrayEquals(data, new Integer[]{1, null, 3});
    }

    @Test
    public void testCase3() {
        var codec = new Codec();
        TreeNode root = codec.deserialize(new Integer[]{1, null, 2});
        Integer[] serialized_tree = codec.serialize(root);
        Assert.assertArrayEquals(serialized_tree, new Integer[]{1, null, 2});

    }

    @Test
    public void testCase4() {
        var codec = new Codec();
        TreeNode root = codec.deserialize(new Integer[]{1, null, 2, 3, null, null, 5});
        Integer[] serialized_tree = codec.serialize(root);
        Assert.assertArrayEquals(serialized_tree, new Integer[]{1, null, 2, 3, null, null, 5});

    }

    @Test
    public void testCase5() {
        var codec = new Codec();
        TreeNode root = codec.deserialize(new Integer[]{1, null, 2, 3, null, null, 5});
        Assert.assertEquals(root.val, 1);
        Assert.assertEquals(root.right.left.val, 3);
        Assert.assertEquals(root.right.left.right.val, 5);

    }

    @Test
    public void testCase6() {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);
        root.right.left.right = new TreeNode(4);

        var codec = new Codec();
        Integer[] data = codec.serialize(root);
        Assert.assertArrayEquals(data, new Integer[]{1, null, 2, 3, null, null, 4});

    }




}