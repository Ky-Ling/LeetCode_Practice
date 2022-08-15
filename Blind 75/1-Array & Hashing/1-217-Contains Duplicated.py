from typing import List

from attr import has

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # (1): Brute force: O(n ^ 2), O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # (2): Sorting: O(nlogn) O(1)
        # nums.sort()

        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        # (3): HashSet:  O(n) O(n)
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False
 

s = Solution()
print(s.containsDuplicate([1, 3, 4]))
