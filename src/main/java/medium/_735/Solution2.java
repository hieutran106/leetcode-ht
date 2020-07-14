package medium._735;

/*
*
* overall, there are totally 4 scenarios will happen: 1.+ + 2.- - 3.+ - 4.- +
        when collision happens: only 3 which is + -
        use a stack to keep track of the previous and compare current value with previous ones
* */

import java.util.Stack;

public class Solution2 {
    public int[] asteroidCollision(int[] asteroids){
        if (asteroids == null) {
            return null;
        } else if (asteroids.length <=1) {
            return  asteroids;
        }

        Stack<Integer> stack = new Stack<>();
        for (int cur: asteroids) {
            if (cur > 0) { // previous one does not matter, no collision forever
                stack.push(cur);
            }

            while (!stack.isEmpty() && stack.peek() > 0 && -cur > stack.peek()) {
                // destroy previous one
                stack.pop();
            }
            if (stack.isEmpty() || stack.peek() < 0) {
                stack.push(cur);
            } else if (stack.peek() == -cur) {
                stack.pop();
            }
        }
        return stack.stream().mapToInt(i -> i).toArray();
    }
}
