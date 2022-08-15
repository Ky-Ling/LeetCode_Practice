from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1

        return -1





s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))


            

    