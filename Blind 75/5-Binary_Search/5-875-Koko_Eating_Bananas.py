import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

            
        return res

s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([30,11,23,4,20], 5))
print(s.minEatingSpeed([30,11,23,4,20], 6))
