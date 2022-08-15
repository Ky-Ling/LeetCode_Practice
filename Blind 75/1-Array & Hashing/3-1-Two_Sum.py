from tkinter import N
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (1): Brute force: O(n * n)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return 
        
        
        # (2): O(n) O(n)
        # In the hashmap, we are going to be mapping the value to to the index
        
        # It stores all the elements that comes before the current  
        # val : index

        # preMap = {}

        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in preMap:
        #         return [preMap[diff], i]

        #     preMap[n] = i
        
        # return 
 


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
 