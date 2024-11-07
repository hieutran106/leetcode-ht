import { describe, expect, test } from "vitest";

function knapsack(weights: number[], values: number[], capacity) {
    const n = weights.length;
    const memo = {};
    function dfs(i: number, remaining_capacity: number): number {
        if (i == n || remaining_capacity == 0) {
            return 0;
        }
        let result: number;
        if (weights[i] > remaining_capacity) {
            result = dfs(i + 1, remaining_capacity);
        } else {
            const include = values[i] + dfs(i + 1, remaining_capacity - weights[i]);
            const exclude = dfs(i + 1, remaining_capacity);
            result = Math.max(include, exclude);
        }

        return result;
    }

    return dfs(0, capacity);
}

describe("knapsack test", () => {
    test("test case 1", () => {
        const actual = knapsack([2, 3, 1, 4], [4, 5, 3, 7], 5);
        expect(actual).toBe(10);
    });

    test("test case 2", () => {
        const actual = knapsack([1, 2, 3, 5], [1, 6, 10, 16], 7);
        expect(actual).toBe(22);
    });

    test("test case 3", () => {
        const actual = knapsack([1, 2, 3, 5], [1, 6, 10, 16], 6);
        expect(actual).toBe(17);
    });
});
