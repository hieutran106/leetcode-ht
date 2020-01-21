package medium._211;





        import org.junit.Test;

        import static org.junit.Assert.assertArrayEquals;
        import static org.junit.Assert.assertEquals;


public class MyTests {
    @Test
    public void justAnExample() {

        var wordDict = new WordDictionary();
        wordDict.addWord("bad");
        wordDict.addWord("dad");
        wordDict.addWord("mad");

        assertEquals(false, wordDict.search("pad"));
        assertEquals(true, wordDict.search("bad"));
        assertEquals(true, wordDict.search(".ad"));
        assertEquals(true, wordDict.search("b.."));

    }


}

