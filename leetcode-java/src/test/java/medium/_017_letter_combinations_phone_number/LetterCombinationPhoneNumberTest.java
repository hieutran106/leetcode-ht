package medium._017_letter_combinations_phone_number;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;

public class LetterCombinationPhoneNumberTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.letterCombinations("23");
        var expect = Arrays.asList("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf");
        Assert.assertEquals(new HashSet<>(actual), new HashSet<>(expect));
    }
}
