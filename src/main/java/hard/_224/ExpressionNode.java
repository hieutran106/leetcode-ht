package hard._224;

public interface ExpressionNode {
    public static final int NUMBER_NODE = 1;
    public static final int PARENTHESIS_NODE = 2;
    public static final int PLUSMINUS_NODE = 3;


    public int getType();
    public int getValue();
}



class NumberNode implements ExpressionNode {
    private int value;
    public NumberNode(int value) {
        this.value = value;
    }
    public int getType() {
        return NUMBER_NODE;
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
    public int getType() {
        return PARENTHESIS_NODE;
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
        int x=  this.op == '+' ? this.lhs.getValue() + this.rhs.getValue() :this.lhs.getValue() - this.rhs.getValue();
        return x;
    }
    public int getType() {
        return PLUSMINUS_NODE;
    }
}

