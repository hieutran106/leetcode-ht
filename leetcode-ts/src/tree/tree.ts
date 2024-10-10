import { expect, test, describe } from "vitest";

export class TreeNode {
    constructor(
        public val: number = 0,
        public left?: TreeNode,
        public right?: TreeNode
    ) {}
}

export function serialize(root: TreeNode) {
    if (root === undefined) {
        return "";
    }
    const q: Array<TreeNode | undefined> = [root];
    const result: Array<number | string> = [];
    while (q.length > 0) {
        const currentNode = q.shift();
        if (currentNode === undefined) {
            result.push("null");
        } else {
            result.push(currentNode.val);
            q.push(currentNode.left);
            q.push(currentNode.right);
        }
    }
    // Remove trailing null
    while (result[result.length - 1] === "null") {
        result.pop();
    }

    return result.join(",");
}

describe("Serialize and Deserialize Binary Tree", () => {
    test("Serialize", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);
        const actual = serialize(root);
        console.log(actual + "help");
        expect(actual).toEqual("1,2,3,null,null,4,5");
    });
});
