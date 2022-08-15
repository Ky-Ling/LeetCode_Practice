from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            
            # It is a sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            mid = (l + r) // 2
            res = min(res, nums[mid])

            # Move to right sorted portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res



s = Solution()

print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17]))