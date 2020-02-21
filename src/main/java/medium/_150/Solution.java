package medium._150;

import org.xml.sax.ext.LexicalHandler;

import java.util.Stack;

public class Solution {
    public int evalRPN(String[] tokens) {
        var stack = new Stack<Integer>();
        for (int i =0; i < tokens.length; i++) {
            var element = tokens[i];
            if (isNumber(element)) {
                stack.push(Integer.parseInt(element));
            } else {
                var lhs = stack.pop();
                var rhs = stack.pop();

                var op = element.charAt(0);

                var result = 0;
                if (op == '+') {
                    result = rhs + lhs;
                } else if (op == '-') {
                    result = rhs - lhs;
                } else if (op == '*') {
                    result = rhs * lhs;
                } else if (op == '/') {
                    result = rhs / lhs;
                }
                stack.push(result);
            }
        }
        if (stack.size() == 1) {
            return stack.pop();
        } else return -1;
    }

    public boolean isNumber(String input) {
        if (input.length() > 1) {
            return true;
        }
        var op = input.charAt(0);
        if (op == '+' || op  == '-' || op == '*' || op == '/') {
            return false;
        }
        return true;
    }

}
