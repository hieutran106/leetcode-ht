package medium._211;

import java.util.HashMap;

public class WordDictionary {

    Node head;
    static final char HEAD_CHARACTOR = '*';

    class Node {
        int value;
        boolean isWord;
        HashMap<Character, Node> children;
        int prefixes;

        public Node(int value) {
            this.value = value;
            this.isWord = false;
            this.children = new HashMap<Character, Node>();
        }
    }

    public WordDictionary() {
        this.head = new Node(HEAD_CHARACTOR);
    }

    private void addNode(Node node, String word) {
        if (word.length() == 0) {
            return;
        }

        var letter = word.charAt(0);
        var child = node.children.get(letter);

        if (child == null) {
            child = new Node(letter);
            node.children.put(letter, child);
        }

        var remainder = word.substring(1);
        if (remainder.length() ==0) {
            child.isWord = true;
        }
        this.addNode(child, remainder);
    }

    public void addWord(String word) {
        this.addNode(this.head, word);
    }

    public boolean search(String word) {
        var node = this.head;
        return this.dfs(node, word);
    }

    public boolean dfs(Node node, String word) {
        if (word.length() == 0) {
            return node.isWord;
        }

        if (word.charAt(0) == '.') {
            var childrenNodes = node.children.values();
            for (var childNode: childrenNodes ) {
                if (this.dfs(childNode, word.substring(1))) {
                    return true;
                }
            }
            return  false;
        } else {
            var check = node.children.get(word.charAt(0));
            if (check == null) {
                return false;
            }
            return this.dfs(check, word.substring(1));
        }
    }
}
