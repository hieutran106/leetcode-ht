package hard._068;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;


public class TextJustificationTest {
    @Test
    public void testCase1() {
        var input = new String[]{"This", "is", "an", "example", "of", "text", "justification."};
        var s = new Solution();
        var result = s.fullJustify(input, 16);

        List<String> expected = Arrays.asList("This    is    an", "example  of text", "justification.  ");
        Assert.assertEquals(result, expected);
    }

    @Test
    public void testCase2() {
        var input = new String[]{"What","must","be","acknowledgment","shall","be"};
        var s = new Solution();
        var result = s.fullJustify(input, 16);

        List<String> expected = Arrays.asList("What   must   be", "acknowledgment  ", "shall be        ");
        Assert.assertEquals(result, expected);
    }

    @Test
    public void testCase3() {
        var input = new String[]{"Science","is","what","we","understand","well","enough","to","explain",
                "to","a","computer.","Art","is","everything","else","we","do"};
        var s = new Solution();
        var result = s.fullJustify(input, 20);

        List<String> expected = Arrays.asList("Science  is  what we", "understand      well", "enough to explain to",
        "a  computer.  Art is", "everything  else  we", "do                  ");
        Assert.assertEquals(result, expected);
    }

    @Test
    public void testCase4() {
        var input = new String[]{"a","aaaa","b","c", "aaaa", "b", "c"};
        var s = new Solution();
        var result = s.fullJustify(input, 4);

        List<String> expected = Arrays.asList("a   ", "aaaa", "b  c", "aaaa", "b c ");
        Assert.assertEquals(result, expected);
    }
}
