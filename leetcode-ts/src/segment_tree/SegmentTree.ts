import { TreeNode } from "../tree/tree";

function calculateSegmentTreeSize(n: number) {
    const height = Math.ceil(Math.log2(n));
    return Math.pow(2, height + 1) - 1;
}

type Range = {
    start: number;
    end: number;
};

export class SegmentTreeNode {
    constructor(
        public val: number = 0,
        public range: Range, // Index range in the original array
        public left?: SegmentTreeNode,
        public right?: SegmentTreeNode
    ) {}
}

class SegmentTree {
    internal: SegmentTreeNode;
    constructor(nums: number[]) {
        this.internal = this.buildHelper(nums, 0, nums.length - 1);
    }

    buildHelper(nums: number[], left: number, right: number): SegmentTreeNode {
        if (left === right) {
            return new SegmentTreeNode(nums[left], { start: left, end: right });
        }
        const mid = Math.floor((left + right) / 2);
        const leftNode = this.buildHelper(nums, left, mid);
        const rightNode = this.buildHelper(nums, mid + 1, right);
        const val = leftNode.val + rightNode.val;
        const node = new SegmentTreeNode(val, { start: leftNode.range.start, end: rightNode.range.end }, leftNode, rightNode);
        return node;
    }

    query(left: number, right: number) {
        return this.queryHelper(this.internal, left, right);
    }

    /**
     *
     * @param nodeIndex index of current node
     * @param start node range
     * @param end node range
     * @param left query range
     * @param right query range
     */
    private queryHelper(node: SegmentTreeNode, left: number, right: number) {
        const { start, end } = node.range;
        // If query range contains node range
        if (left <= start && end <= right) {
            return node.val;
        }
        // If not overlapping
        if (end < left || right < start) {
            return 0; // return identity value, 0 for range sum
        }
        // partially overlap
        const leftValue = this.queryHelper(node.left!, left, right);
        const rightValue = this.queryHelper(node.right!, left, right);
        return leftValue + rightValue;
    }

    update(index: number, val: number) {
        this.updateHelper(this.internal, index, val);
    }

    private updateHelper(node: SegmentTreeNode, index: number, val: number) {
        const { start, end } = node.range;
        // Out of range
        if (index < start || index > end) {
            return node.val;
        }
        // Index in the range
        if (start === end) {
            node.val = val;
            return val;
        }

        const leftValue = this.updateHelper(node.left!, index, val);
        const rightValue = this.updateHelper(node.right!, index, val);
        node.val = leftValue + rightValue;
        return node.val;
    }
}
export { SegmentTree };
