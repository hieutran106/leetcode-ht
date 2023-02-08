from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list
        # map each course to prerequisite list
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # a course has 3 possible states:
        # visited  -> course has been added to ouput
        # visiting -> course not added to output, but currently being visiting
        # unvisited -> course not added to output and not being visiting
        output = []
        visited = set()
        # set to detect a cyle
        visiting = set()

        def dfs(course) -> bool:
            """Return False if there is a cycle"""
            if course in visiting:
                # there is a cycle
                return False

            if course in visited:
                # already visited, not visit this node again
                return True

            visiting.add(course)
            for pre in pre_map[course]:
                if dfs(pre) == False:
                    return False

            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output