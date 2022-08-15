from itertools import count
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # (1): Brute force: O(n ^ 2)
        # if len(nums1) == 0 or len(nums2) == 0:
        #     return []
        
        # if not nums1 or not nums2:
        #     return -1

        # res = []

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j] and nums1[i] not in res:
        #             res.append(nums1[i])
        
        # return res

        # (2):
        stack = []
        for i in nums1:
            if i in nums2:
                stack.append(i)
        
        return stack

        
        

s = Solution()

# print(s.intersection([1,2,2,1], [2,2]))
# print(s.intersection([1,2,2,1], [3]))
# print(s.intersection([], [9,4,9,8,4]))
# print(s.intersection([5], [9,4,9,8,4]))
print(s.intersection([4,9,5], [9,4,9,8,4]))