package easy._268_missing_number;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MisisngNumberTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.missingNumber(new int[]{3, 0, 1});
        assertEquals(2, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.missingNumber(new int[]{0, 1});
        assertEquals(2, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.missingNumber(new int[]{9,6,4,2,3,5,7,0,1});
        assertEquals(8, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.missingNumber(new int[]{0});
        assertEquals(1, actual);
    }



}