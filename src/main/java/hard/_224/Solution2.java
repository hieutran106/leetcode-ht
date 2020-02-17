package hard._224;

import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution2 {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();

        int result = 0;



        int index = 0;
        int sign = 1;

        while (index < s.length()) {
            int step = 1;
            if (s.charAt(index) == '+') {
                sign = 1;
            } else if (s.charAt(index) == '-') {
                sign = -1;
            } else if (s.charAt(index) == ' ') {
                // do nothing
            } else if (s.charAt(index) == '(') {
                stack.push(0);
            } else  if (s.charAt(index) == ')') {
                result = result + sign * stack.pop();
            } else {
                Pattern pattern = Pattern.compile("^([0-9]+)");
                Matcher match = pattern.matcher(s);

                if (match.find()) {
                    String numberStr = s.substring(match.start(), match.end());
                    int number = Integer.parseInt(numberStr);
                    step = match.end() - match.start();

                    if (!stack.isEmpty()) {
                        stack.push(stack.pop() + sign * number);
                    } else {
                        result += sign * number;
                    }
                } else {
                    System.out.println("Invalid input string");
                    return -1;
                }
            }
            index += step;
        }
        return result;
    }
}
