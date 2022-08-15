from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Time: O(nlogn)
        
        intervals.sort(key=lambda i : i.start )

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True


s = Solution()
print(s.can_attend_meetings([(0,30),(5,10),(15,20)]))    
print(s.can_attend_meetings([(5,8),(9,15)]))    

