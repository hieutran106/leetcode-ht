package hard._224;

import java.util.LinkedList;
import java.util.List;

public class Parser {
    LinkedList<Token> tokens;
    Token lookahead;

    public ExpressionNode parse(List<Token> tokens) throws Exception {
        this.tokens = new LinkedList<>();
        for (int i =0; i < tokens.size(); i ++) {
            this.tokens.add(tokens.get(i));
        }
        //this.tokens = (LinkedList<Token>) tokens.clone();
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

    private ExpressionNode expression_prime(ExpressionNode expr) {
        if (lookahead.type == TokenType.PLUS) {
            nextToken();
            ExpressionNode child = expression_prime(expr);
            return new PlusMinusNode(expr, child, '+');
        } else if (lookahead.type == TokenType.MINUS) {
            nextToken();
            ExpressionNode child = expression_prime(expr);
            return new PlusMinusNode(expr, child, '-');
        } else if (lookahead.type == TokenType.NUMBER)  {
            nextToken();
            ExpressionNode child = new NumberNode(Integer.parseInt(lookahead.token));
            return child;
        }

        return expr;
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
            nextToken();
            return new NumberNode(Integer.parseInt(lookahead.token));
        } else {
            throw new Exception("Term end");
        }

    }
}
