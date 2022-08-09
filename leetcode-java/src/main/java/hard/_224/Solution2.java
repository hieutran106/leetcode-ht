package hard._224;


import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class StackElement {
    int value;
    int sign;
    public StackElement(int value, int sign) {
        this.value = value;
        this.sign = sign;
    }
}

public class Solution2 {
    public int calculate(String s) {
        Stack<StackElement> stack = new Stack<StackElement>();
        int result = 0;
        int index = 0;
        int sign = 1;
        while (s.length() > 0) {
            int step = 1;
            if (s.charAt(index) == '+') {
                sign = 1;
            } else if (s.charAt(index) == '-') {
                sign = -1;
            } else if (s.charAt(index) == ' ') {
                // do nothing
            } else if (s.charAt(index) == '(') {
                stack.push(new StackElement(0, sign));
                sign = 1;
            } else  if (s.charAt(index) == ')') {
                StackElement ele = stack.pop();
                if (!stack.isEmpty()) {
                    StackElement element = stack.peek();
                    element.value = element.value + ele.sign * ele.value;
                } else {
                    result = result + ele.sign * ele.value;
                }

            } else {
                Pattern pattern = Pattern.compile("^([0-9]+)");
                Matcher match = pattern.matcher(s);


                if (match.find()) {
                    String numberStr = s.substring(match.start(), match.end());
                    int number = Integer.parseInt(numberStr);
                    step = match.end() - match.start();

                    if (!stack.isEmpty()) {
                        StackElement element = stack.peek();
                        element.value = element.value + sign * number;
                    } else {
                        result += sign * number;
                    }
                } else {
                    System.out.println("Invalid input string");
                    return -1;
                }
            }
            s = s.substring(step);
        }
        return result;
    }
}
