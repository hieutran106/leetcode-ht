import { expect, test, describe } from "vitest";
import { SegmentTree } from "./SegmentTree";
import { serialize } from "../tree/tree";

describe("segment tree test", () => {
    test("test case 1", () => {
        const tree = new SegmentTree([3, 4, 10, 2, 7]);
        const internal = tree["internal"];
        const nodes = serialize(internal);
        expect(nodes).toEqual("26,17,9,7,10,2,7,3,4");
    });

    test("test case 2", () => {
        const tree = new SegmentTree([3, 4, 10, 2, 7]);
        const actual = tree.query(0, 4);
        expect(actual).toEqual(26);
    });

    test("test case 3", () => {});
});
