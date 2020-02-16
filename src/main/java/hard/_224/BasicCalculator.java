package hard._224;

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BasicCalculator {
    public ArrayList<Token> tokenize(String str) {
        var result = new ArrayList<Token>();
        String s = new String(str);
        while(!s.isEmpty()) {
            int length = 1;
            if (s.charAt(0) == '(') {
                result.add(new Token(s.substring(0, 1), TokenType.LPARENT));
            } else if (s.charAt(0) == ')'){
                result.add(new Token(s.substring(0, 1), TokenType.RPARENT));
            } else if (s.charAt(0) == '+') {
                result.add(new Token(s.substring(0, 1), TokenType.PLUS));
            } else if (s.charAt(0) == '-') {
                result.add(new Token(s.substring(0, 1), TokenType.MINUS));
            } else if (s.charAt(0) == ' ') {
                // skip do nothin

            } else {
                Pattern pattern = Pattern.compile("^([0-9]+)");
                Matcher match = pattern.matcher(s);

                if (match.find()) {
                    var token = new Token(s.substring(match.start(), match.end()), TokenType.NUMBER);
                    result.add(token);
                    length = match.end() - match.start();
                } else {
                    System.out.println("Invalid input string");
                }
            }

            s = s.substring(length);
        }
        return result;
    }

    public ExpressionNode parse(ArrayList<Token> tokens) throws Exception {
        Parser parser = new Parser();
        ExpressionNode node = parser.parse(tokens);
        return node;
    }
}


enum TokenType {
    LPARENT,
    RPARENT,
    PLUS,
    MINUS,
    NUMBER,
    EPSILON
}

class Token {
    public String token;
    public TokenType type;


    public Token(String token, TokenType type ) {
        this.token = token;
        this.type = type;
    }

}