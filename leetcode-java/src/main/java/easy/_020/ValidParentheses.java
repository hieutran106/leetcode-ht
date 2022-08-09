package easy._020;

import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        var open = "([{";
        var close = ")]}";

        Stack<Character> stack = new Stack<>();
        for (int i =0; i < s.length(); i ++) {
            var c = s.charAt(i);
            if (open.indexOf(c) != -1) {
                stack.push(c);
                continue;
            }

            // handle close parentheses
            if (stack.isEmpty()) {
                return false;
            }

            // pop element at the top of stack
            var top = stack.peek();
            if (c == close.charAt(open.indexOf(top))) {
                stack.pop();
            } else return false;


        }

        return stack.size() == 0;
    }
}
