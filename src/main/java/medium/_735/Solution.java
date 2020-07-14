package medium._735;

import java.util.Arrays;


public class Solution {
    public int[] asteroidCollision(int[] asteroids) {

        if (asteroids.length < 2) {
            return asteroids;
        }
        for (int i = asteroids.length-2; i >=0; i --) {
            for (int j = i + 1; j < asteroids.length;j ++) {

                if (asteroids[i] < 0 || asteroids[j] > 0) {
                    continue;
                }
                int value = asteroids[i] + asteroids[j];
                if (value ==0) {
                    asteroids[j] = 0;
                    asteroids[i] = 0;
                } else if (value > 0) {
                    asteroids[j] = 0;
                } else {
                    asteroids[i] = asteroids[j];
                    asteroids[j] = 0;
                }
            }

        }

        var result = Arrays.stream(asteroids).filter(x -> x !=0).toArray();
        return result;
    }

    public int[] asteroidCollision2(int[] asteroids) {

        if (asteroids.length < 2) {
            return asteroids;
        }
        for (int i = asteroids.length-2; i >=0; i --) {
            int j = i + 1;
            if (asteroids[i] < 0 || asteroids[j] > 0) {
                continue;
            }
            int value = asteroids[i] + asteroids[j];
            if (value ==0) {
                asteroids[j] = 0;
                asteroids[i] = 0;
            } else if (value > 0) {
                asteroids[j] = 0;
            } else {
                asteroids[i] = asteroids[j];
                asteroids[j] = 0;
            }
        }

        var result = Arrays.stream(asteroids).filter(x -> x !=0).toArray();
        return result;
    }
}
