package easy._190_reverse_bits;

import java.util.ArrayList;

public class Solution {
    public int reverseBits(int n) {
        String binaryRep = toBinaryString(n);
        return reverse(binaryRep);
    }

    public String toBinaryString(int n) {
        if (n == Integer.MIN_VALUE) {
            return "10000000000000000000000000000000";
        }
        int value = n >=0 ? n : -n;
        StringBuilder sb = new StringBuilder(32);
        while (value > 0) {
            int r = value % 2;
            sb.append(r);
            value = value / 2;
        }

        // padding
        while (sb.length() < 32) {
            sb.append('0');
        }
        String positive = sb.reverse().toString();
        System.out.println("Positive:" + prettyPrint(positive));
        if (n >=0) {
            return positive;
        }

        String negative = getTwoComplement(positive);
        System.out.println("Negative:" + prettyPrint(negative));
        return negative;
    }

    public String getTwoComplement(String positiveRepresent) {
        char[] rep = positiveRepresent.toCharArray();
        int index = -1;
        // find the index of 1 from the end
        for (int i = rep.length -1; i >=0; i--) {
            if (rep[i] == '1') {
                index = i;
                break;
            }
        }
        // flip
        for (int i =0; i < index; i++) {
            rep[i] = rep[i] == '0' ? '1' : '0';
        }

        String result = new String(rep);
        return result;
    }


    public String prettyPrint(String binaryRepresentation) {
        if (binaryRepresentation.length() != 32) {
            return "Invalid format";
        }

        ArrayList<String> result = new ArrayList<>();
        for (int i =0; i < 32; i = i + 4) {
            String sub = binaryRepresentation.substring(i, i + 4);
            result.add(sub);
        }
        return String.join("_", result);
    }

    public int reverse(String binaryRep) {
        int sum = 0;
        sum += Math.pow(2, 31) * -1 * (binaryRep.charAt(31) == '1' ? 1 : 0);
        for (int i = 30; i >=0; i--) {
            sum+= (binaryRep.charAt(i) == '1' ? 1 : 0) * Math.pow(2, i);
        }
        return sum;
    }

}

