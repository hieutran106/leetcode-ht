from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list
        # map each course to prerequisite list
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # store all visited course,
        # if a course is in global_set, it means that there is no clycle from this node
        global_visit = set()

        def is_cyclic(c, visit: Set[int]):
            """Is there a cycle from current course?"""
            if c in visit:
                # If we already visited current course along the current DFS path,
                # there must be cyclic
                return True
            visit.add(c)
            for pre_course in pre_map[c]:
                if pre_course in global_visit:
                    continue
                if is_cyclic(pre_course, visit):
                    return True
            # backtrack
            visit.remove(c)
            # No cycle found, return False
            return False

        for course in range(numCourses):
            visit = set()
            if is_cyclic(course, visit):
                return False
            global_visit.add(course)

        return True
