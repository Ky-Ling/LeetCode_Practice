from typing import List
import heapq


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute force: O(nlogn) --> sorting
        res = []
        ans = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            res.append([distance, x, y])

        while k > 0:

            distance, x, y = sorted(res, reverse=True).pop()
            ans.append([x, y])
            k -= 1
        
        return ans
        

        # return (sorted(res)[:k])[k-1][1:]
    
        
        # (2): minHeap: O(klogn)

        # minHeap = []

        # for x, y in points:
        #     distance = (x ** 2) + (y ** 2)
        #     minHeap.append([distance, x, y])

        # heapq.heapify(minHeap)
        # res = []

        # while k > 0:
        #     distance, x, y = heapq.heappop(minHeap)
        #     res.append([x, y])
        #     k -= 1

        # return res      
        


s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))

