package medium._1155;


public class Solution {
    public int numRollsToTarget(int d, int f, int target) {
//        System.out.println(String.format("Calculating case [d=%d, f=%d, target=%d", d,f,target));

        int[][][] cache = new int[d][f][target];

        for (int i = 0; i < d; i++)
            for (int j=0; j < f; j++)
                for (int k=0; k < target; k++)
                    cache[i][j][k] = -1;

        long result = helper(d,f ,target, 0, cache);
        int mod = (int)Math.pow(10, 9) + 7;

        return (int)(result % mod);
    }

    private int helper(int d, int f, int target, int indent, int[][][] cache) {

        if (target <=0) {
            return 0;
        }
        // base-case
        if (d ==1) {
            return f >= target ? 1 : 0;
        }

        if (target < d || target > f*d) {
            return 0;
        }

        if (cache[d-1][f-1][target-1] != -1) {
            return cache[d-1][f-1][target-1];
        }

        long sum = 0;
        for (int i =1; i <=f; i++) {
            sum = sum + helper(d-1, f, target-i, indent + 1, cache);
        }

        if (sum < 0) {
            System.out.println("Overflow for long");
        }

        int finalResult = (int)(sum % 1000000007);



        cache[d-1][f-1][target-1] = finalResult;
//        if (indent ==1) {
//            System.out.println(".".repeat(indent) + String.format("[d=%d, f=%d, target=%d] -> %d", d,f,target, finalResult));
//        }
        return finalResult;
    }
}
