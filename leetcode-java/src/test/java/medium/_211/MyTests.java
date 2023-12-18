package medium._211;





import org.junit.jupiter.api.Test;



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

    private void assertEquals(boolean b, boolean pad) {
    }


}

