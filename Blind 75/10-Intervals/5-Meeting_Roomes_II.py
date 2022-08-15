from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Time: O(nlogn), memory: O(n)

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
                                                                                                                                                                                    
        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1

            # If they are equal too, we wanna increment e pointer first
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
