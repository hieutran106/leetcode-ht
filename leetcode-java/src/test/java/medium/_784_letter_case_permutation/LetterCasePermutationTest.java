package medium._784_letter_case_permutation;

import org.assertj.core.api.Assertions;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class LetterCasePermutationTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.letterCasePermutation("3z4");
        assertArrayEquals(actual.toArray(), new String[]{"3z4", "3Z4"});
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.letterCasePermutation("12345");
        assertArrayEquals(actual.toArray(), new String[]{"12345"});
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.letterCasePermutation("a1b2");
        assertEquals(actual.size(), 4);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.letterCasePermutation("");
        assertEquals(actual.size(), 1);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.letterCasePermutation("a1b2");
        Assertions.assertThat(actual).containsExactlyInAnyOrder("a1b2","a1B2","A1b2","A1B2");
    }
}
