from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # The right pointer is scanning through the entire array. and the left pointer
        #   is telling us where we are going to put the next unique value, it tells us
        #   how many unique values we have already seen so far.
        
        # O(2 * n) = O(n)
        
        # Initially the first value alway in order. We set left and right pointers are in 1-index

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] == nums[r]
                l += 1

        return l


s = Solution()

print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
