from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # (1): Sorting Solution: O(nlogn)
        # (2): Iterate the initial array, convert this array into a set and use it. Check if
        #   values have left neighbors and if they did not, they will start the sequence
        #   --> Time and Memory: O(n)
        
        numSet = set(nums)
        longest = 0

        for s in nums:
            if (s - 1) not in numSet:
                length = 0

                while (s + length) in numSet:
                    length += 1

                longest = max(longest, length)

        return longest


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1, 2, 3]))