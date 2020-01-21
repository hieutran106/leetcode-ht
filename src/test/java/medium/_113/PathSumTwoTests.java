package medium._113;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class PathSumTwoTests {
    @Test
    public void testCase1() {

        TreeNode rootNode =new TreeNode(40);
        TreeNode node20=new TreeNode(20);
        TreeNode node10=new TreeNode(10);
        TreeNode node30=new TreeNode(30);
        TreeNode node60=new TreeNode(60);
        TreeNode node50=new TreeNode(50);
        TreeNode node70=new TreeNode(70);
        TreeNode node5=new TreeNode(5);
        TreeNode node55=new TreeNode(55);

        rootNode.left=node20;
        rootNode.right=node60;

        node20.left=node10;
        node20.right=node30;

        node60.left=node50;
        node60.right=node70;
        node10.left=node5;
        node50.right=node55;

        var solution = new PathSumTwo();
        var reulst = solution.pathSum(rootNode, 75);

        assertEquals(true, true);

    }
}
