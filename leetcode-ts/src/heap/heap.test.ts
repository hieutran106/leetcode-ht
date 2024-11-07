import { describe, expect, test } from "vitest";
import { MaxHeap, getValue } from "./heap";

describe("max heap test", () => {
    test("test case 1", () => {
        const elements = [70, 50, 40, 45, 35, 39, 16, 10, 9];
        const pq = new MaxHeap(elements);
        pq.insert(60);
        expect(pq.heap).toEqual([70, 60, 40, 45, 50, 39, 16, 10, 9, 35]);
    });

    test("test insert an element to a heap", () => {
        const elements = [50, 40, 30, 17, 13, 12, 11, 7, 4, 6];
        const pq = new MaxHeap(elements);
        pq.insert(43);
        expect(pq.heap).toEqual([50, 43, 30, 17, 40, 12, 11, 7, 4, 6, 13]);
    });

    test("test remove the root node", () => {
        const pq = new MaxHeap([50, 43, 30, 17, 40, 12, 11, 7, 4, 6, 13]);
        const max = pq.pop();
        expect(max).toBe(50);
        const values = pq.heap.map(getValue);
        expect(values).toEqual([43, 40, 30, 17, 13, 12, 11, 7, 4, 6]);
    });

    test("test build a heap from an array", () => {
        const elements = [-1, 1, 5, 0, 0, 4, 6, 7];
        const pq = new MaxHeap(elements);
        expect(pq.heap.map(getValue)).toEqual([7, 1, 6, 0, 0, 4, 5, -1]);
    });
});
