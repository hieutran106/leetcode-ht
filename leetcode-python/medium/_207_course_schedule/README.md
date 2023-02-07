We need to find if the graph has any cycle. If so, we cannot finish all courses, thus return False
To detect cycle, we will run BFS for all nodes (courses) in the graph.
 - Build adjacency list
```python
# build adjacency list
# map each course to prerequisite list
pre_map = {i: [] for i in range(numCourses)}
for course, pre in prerequisites:
    pre_map[course].append(pre)
```
 - `def is_cyclic(c, visit: Set[int]):` a recursive DFS function to detect cycle
 - We use a set `global_visit = set()` to store visited nodes. If a course in the set, there is no cycle from this node.