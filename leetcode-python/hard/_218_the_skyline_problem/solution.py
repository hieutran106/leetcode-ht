from typing import List
import heapq
from collections import deque

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def addSkyline(skyline: List[int], point):
            if not skyline:
                skyline.append(point)
                return
            if skyline[-1][1] != point[1]:
                skyline.append(point)

        keypoints_list = []
        for l,r,h in buildings:
            keypoints_list.append((l, h, 'L'))
            keypoints_list.append((r, h, 'R'))
        keypoints_list.sort()
        keypoints = deque(keypoints_list)
        # print(f"{keypoints=}")
        skyline = []
        max_heap = [0] # Store (-height), have ground - 0 by default
        while keypoints:
            # Look at left most item in queue
            curr_height = keypoints[0][0]
            while keypoints and keypoints[0][0] == curr_height:
                # Pull all point with current height
                pos, h, type = keypoints.popleft()
                if type == 'L':
                    heapq.heappush(max_heap, (-h))
                elif type == 'R':
                    max_heap.remove(-h)
                    heapq.heapify(max_heap)

            max_height = -max_heap[0]
            # add max_height to skyline
            # print(f"At {pos=}, {max_height=}")
            addSkyline(skyline, point=[pos, max_height])

        return skyline
