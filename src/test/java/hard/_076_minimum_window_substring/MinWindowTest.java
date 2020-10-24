package hard._076_minimum_window_substring;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.Assert.*;

public class MinWindowTest {
    private Path workingDir;

    @Before
    public void init() {
        this.workingDir = Path.of("", "src/test/java/hard/_076_minimum_window_substring");
    }

    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.minWindow("ADOBECODEBANC", "ABC");
        Assert.assertEquals("BANC", actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.minWindow("CBA", "A");
        Assert.assertEquals("A", actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.minWindow("", "A");
        Assert.assertEquals("", actual);
    }


    @Test
    public void testCase5() throws IOException {


        Path fileName = this.workingDir.resolve("test_case_267_str_s.txt");
        String s = Files.readString(fileName);

        fileName = this.workingDir.resolve("test_case_267_str_t.txt");
        String t = Files.readString(fileName);

        fileName = this.workingDir.resolve("test_case_267_expect.txt");
        String expect = Files.readString(fileName);

        var solution = new Solution();
        var actual = solution.minWindow(s, t);

        Assert.assertEquals(expect, actual);


    }
}