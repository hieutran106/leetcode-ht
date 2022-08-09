package medium._238;

public class ProductOfArray {
    public int[] productExceptSelf(int[] nums) {

        int[] result = new int[nums.length];
        int[] tail = new int[nums.length];
        tail[0] = 1;

        for (int i =1; i < nums.length; i ++) {
            //head[i] = nums[i-1] * head[i -1];
            int j = nums.length - i;
            tail[i] = nums[j] * tail[i-1];
        }

        int sum = 1;
        for (int i =0; i < nums.length; i ++) {
            int j =  (nums.length-1) - i;
            result[i] = sum * tail[j];
            sum = sum * nums[i];
        }

        return result;
        
    }


}
