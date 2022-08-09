package medium._075;




import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;


public class MyTests {
    @Test
    public void justAnExample() {
       int[] input = new int[]{2, 0, 2, 1, 1, 0};
       var solution = new Solution();
       solution.sortColors(input);
       assertArrayEquals(new int[]{0,0,1,1,2,2}, input);


    }


}

