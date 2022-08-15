from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # (1): Brute force: O(nlogn)
        # return sorted(nums, reverse=True)[k-1]

        # (2): minHeap: O(n + klogn)
        # heapq.heapify(nums)

        # for i in range(len(nums) - k):
        #     # Pop out: O(klogn) --> Pop once is logn, k times is klogn
        #     heapq.heappop(nums)

        # return nums[0]
        

 
        # (3): O(n) average time complexity, worse case -> O(n*2)
        # Quick Select
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
            
        return quickSelect(0, len(nums) - 1)



s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(s.findKthLargest([-1, -1, 3], 1))