from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Because pos and speed are positive, we can sort the vehicles by (pos, speed) pair
        A stack will store the time a car takes to reach the target
            - Iterate through the vehicles
            - If the current time < time at the top of stack => they will form a fleet
            - Finally, the fleet size is the length of stack
        """
        def time_to_target(tup):
            return (target - tup[0]) / tup[1]

        data = sorted(zip(position, speed), key=lambda ele: ele[0], reverse=True)
        stack = []
        for ele in data:
            curr_time = time_to_target(ele)
            if len(stack) > 0 and curr_time <= stack[-1]:
                # form a fleet and move at slower speed
                # thus discard the current vehicle
                pass
            else:
                stack.append(curr_time)
        return len(stack)
