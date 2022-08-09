package hard._068;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        var lines = new ArrayList<String[]>();
        int i = 0;
        while (i < words.length) {

            int j = i + 1;
            while (j < words.length) {
                int minRequiredWidth = minRequiredWidth(words, i, j + 1);
                if (minRequiredWidth > maxWidth) {
                    break;
                }
                j++;
            }
            // 1 line
            String[] line = Arrays.copyOfRange(words, i, j);
            lines.add(line);
            // update index
            i = j;
        }
        // loop for each line

        var result = new ArrayList<String>();

        for (int k =0; k < lines.size(); k++) {
            String[] lineWords = lines.get(k);
            // only 1 word in the line
            String line;
            if (lineWords.length == 1) {
                line = lineWords[0] + " ".repeat(maxWidth - lineWords[0].length());
                result.add(line);
                continue;
            }

            // handle last line
            if (k == lines.size() - 1) {
                line = String.join(" ", lineWords);
                line = line + " ".repeat(maxWidth - line.length());
                result.add(line);
                break;
            }

            // otherwise
            String[] spaces = padSpace(lineWords, maxWidth);
            StringBuilder builder = new StringBuilder(maxWidth);
            for (int j=0; j < lineWords.length;j ++) {
                var word = lineWords[j];
                builder.append(word);
                if (j < spaces.length) {
                    builder.append(spaces[j]);
                }
            }
            result.add(builder.toString());
        }
        return result;
    }

    private int minRequiredWidth(String[] words, int start, int end) {
        int len = end - start;
        int width = 0;
        for (int i = start; i < end; i ++) {
            width+= words[i].length();
        }
        if (len > 1) {
            // add space between words
            width = width + (len - 1);
        }
        return width;
    }

    private String[] padSpace(String[] words, int maxWidth) {

        int allSpaces = maxWidth - Arrays.asList(words).stream().mapToInt(a -> a.length()).reduce(0, (a,b) -> a + b);

        int numSpace = words.length - 1;
        int quotient = allSpaces / numSpace;
        int remainder = allSpaces - quotient * numSpace;
        int[] numSpaces = new int[numSpace];
        Arrays.fill(numSpaces, quotient);
        for (int i =0; i < remainder; i++) {
            numSpaces[i]++;
        }

        String[] result = new String[numSpaces.length];
        for (int i =0; i < result.length; i++) {
            result[i] = " ".repeat(numSpaces[i]);
        }
        return result;
    }

}
