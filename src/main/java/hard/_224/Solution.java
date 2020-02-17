package hard._224;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    public int calculate(String s) {
        BasicCalculator result = new BasicCalculator();
        var x = result.tokenize(s);
        try {
            var y = result.parse(x);
            var finalResult = y.getValue();
            return finalResult;
        } catch (Exception e) {
            return 0;
        }
    }
}


class BasicCalculator {
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

class Parser {
    LinkedList<Token> tokens;
    Token lookahead;

    public ExpressionNode parse(List<Token> tokens) throws Exception {
        this.tokens = new LinkedList<>();
        for (int i =0; i < tokens.size(); i ++) {
            this.tokens.add(tokens.get(i));
        }
        lookahead = this.tokens.getFirst();

        ExpressionNode topExpr = expression();
        if (lookahead.type != TokenType.EPSILON) {
            throw new Exception("Unexpected symbol %s found" + lookahead.toString());
        }

        return topExpr;
    }

    private void nextToken() {
        tokens.pop();
        // at the end of input we return an epsilon token
        if (tokens.isEmpty()) {
            lookahead = new Token("", TokenType.EPSILON );
        } else {
            lookahead = tokens.getFirst();
        }
    }

    private ExpressionNode expression() throws Exception {
        ExpressionNode termExpr = term();
        ExpressionNode expr = expression_prime(termExpr);
        return expr;
    }

    private ExpressionNode expression_prime(ExpressionNode expr) throws Exception {
        ExpressionNode tLeft = expr;

        if (tLeft == null) {
            tLeft = term();
        }

        while(lookahead.type == TokenType.PLUS || lookahead.type == TokenType.MINUS) {
            char op = lookahead.type == TokenType.PLUS ? '+' : '-';
            nextToken();
            ExpressionNode tRight = term();
            tLeft = new PlusMinusNode(tLeft, tRight , op);
        }
        return tLeft;

    }
    private ExpressionNode term() throws  Exception {
        if (lookahead.type == TokenType.LPARENT) {
            nextToken();
            ExpressionNode childExpr = expression();
            if (lookahead.type != TokenType.RPARENT) {
                throw new Exception("Closing brackets expected");
            }
            nextToken();

            return new ParenthesisNode(childExpr);
        } else if (lookahead.type == TokenType.NUMBER) {
            NumberNode newNode = new NumberNode(Integer.parseInt(lookahead.token));
            nextToken();
            return newNode;
        } else {
            throw new Exception("Term end");
        }
    }
}

interface ExpressionNode {
    int getValue();
}



class NumberNode implements ExpressionNode {
    private int value;
    public NumberNode(int value) {
        this.value = value;
    }


    public int getValue() {
        return this.value;
    }

}

class ParenthesisNode implements ExpressionNode {
    private ExpressionNode node;
    public ParenthesisNode(ExpressionNode node) {
        this.node = node;
    }

    public int getValue() {
        return this.node.getValue();
    }

}

class PlusMinusNode implements  ExpressionNode {
    private ExpressionNode lhs;
    private ExpressionNode rhs;
    char op;
    public PlusMinusNode(ExpressionNode lhs, ExpressionNode rhs, char op) {
        this.lhs = lhs;
        this.rhs = rhs;
        this.op = op;
    }

    public int getValue() {
        return  this.op == '+' ? this.lhs.getValue() + this.rhs.getValue() :this.lhs.getValue() - this.rhs.getValue();
    }

}
