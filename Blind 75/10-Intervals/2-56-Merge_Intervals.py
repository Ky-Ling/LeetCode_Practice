from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) -> Sorting
        
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        lastEnd = output[-1][1]

        for start, end in intervals[1:]:
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)

            else:
                output.append([start, end])

        return output

s = Solution()

print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,3],[2,3]]))