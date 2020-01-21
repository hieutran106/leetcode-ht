package medium._146;

import java.util.HashMap;

public class LRUCache {

    // inline class
    class Node {
        int key;
        int value;
        Node prev;
        Node next;
        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // end - inline class

    Node head, tail;

    HashMap<Integer, Node> cache;

    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;

        this.head = new Node(0,0);
        this.tail = new Node(0,0);
        head.next = tail;
        tail.prev = head;

        cache = new HashMap<>();

    }


    private void addNode(Node node) {

        node.next = head.next;
        node.prev = head;

        head.next.prev = node;
        head.next = node;

    }

    private void removeNode(Node node) {
        var successor = node.prev;
        var predecessor = node.next;

        successor.next = predecessor;
        predecessor.prev = successor;

        node.next = null;
        node.prev = null;
    }

    private void moveToHead(Node node) {
        this.removeNode(node);
        this.addNode(node);
    }

    public int get(int key) {
        var node = cache.get(key);
        if (node == null) {
            return -1;
        }

        // move the node to head;
        this.moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {

        var node = this.cache.get(key);

        if (node != null) {
            node.value = value;
            moveToHead(node);
            return;
        }

        if (cache.size() == capacity) {
            var removedNode = tail.prev;
            removeNode(removedNode);
            cache.remove(removedNode.key);

        }

        // add key to the top
        var newest = new Node(key, value);
        addNode(newest);
        cache.put(key, newest);

    }
}


