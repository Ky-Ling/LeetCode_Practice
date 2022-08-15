from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # (1): Brute force
        while True:
            if len(stones) == 1:
                return stones[0]

            stones = sorted(stones, reverse=True)
            stones.append(stones[0] - stones[1])

            del stones[0:2]
        
        
        # # (2): O(nlogn)
        # # Put them into a min heap and multiply every one of these values by -1
        
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)

        #     # Because they are negative number
        #     if second > first:
        #         heapq.heappush(stones, first - second)

        # # If the stones is empty, finally we will return 0, otherwise we can still return the
        # #   the first element
        # stones.append(0)
        # return abs(stones[0])


s = Solution()

print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([1]))

