package _6xx._703_kth_largest_element_in_stream;

import java.util.PriorityQueue;

class KthLargest {

    PriorityQueue<Integer> queue;
    int k;
    public KthLargest(int k, int[] nums) {
        queue = new PriorityQueue<>(k);
        this.k = k;
        for (int n: nums) {
            queue.add(n);
        }

    }

    public int add(int val) {

        queue.add(val);
        while (queue.size() > k) {
            queue.poll();
        }
        return queue.peek();
    }
}
    