export type NumberOrObject = number | { value: number };

export function getValue(n: NumberOrObject) {
    return typeof n === "number" ? n : n.value;
}

interface Heap {
    peek(): number;
    insert(value: NumberOrObject): void;
}

export class MaxHeap implements Heap {
    heap: NumberOrObject[];
    constructor(data: NumberOrObject[]) {
        this.heap = this.buildHeap(data);
    }

    private buildHeap(data: NumberOrObject[]) {
        const heap = [...data];
        const n = data.length;
        console.log(heap);
        for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
            console.log(`heapifyDown at ${i}`);
            this.heapifyDown(i);
        }
        return heap;
    }
    peek(): number {
        const element = this.heap[0];
        return getValue(element);
    }

    insert(value: NumberOrObject): void {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }
    /**
     * Extract max value
     */
    pop(): number {
        if (this.heap.length == 0) {
            throw new Error("Empty heap");
        }
        this.swap(0, this.heap.length - 1);
        const max = this.heap.pop();
        this.heapifyDown(0);
        return getValue(max!);
    }

    /**
     *
     * @param start
     */
    heapifyDown(start: number) {
        // Compare current element with both children
        // If either child is larger than the current, swap it with the child that has the larger value
        while (2 * start + 1 < this.heap.length) {
            let largest = start;
            const left = 2 * start + 1;
            const right = 2 * start + 2;
            if (getValue(this.heap[left]) > getValue(this.heap[start])) {
                largest = left;
            }
            if (right < this.heap.length && getValue(this.heap[right]) > getValue(this.heap[largest])) {
                largest = right;
            }
            if (largest === start) {
                break;
            }
            this.swap(start, largest);
            start = largest;
        }
    }

    /**
     * Move the value successively up the tree if its parent has smaller value
     * @param start
     */
    heapifyUp(start: number) {
        let childIndex = start;
        while (this.shouldSwap(childIndex)) {
            // swap value
            this.swap(childIndex, this.getParentIndex(childIndex));
            //
            childIndex = this.getParentIndex(childIndex);
        }
    }

    private getParentIndex(childIndex: number): number {
        return Math.floor((childIndex - 1) / 2);
    }

    private shouldSwap(childIndex: number): boolean {
        const parentIndex = this.getParentIndex(childIndex);
        return getValue(this.heap[parentIndex]) < getValue(this.heap[childIndex]);
    }

    private swap(index1: number, index2: number): void {
        [this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]];
    }
}
