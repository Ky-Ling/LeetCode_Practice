from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1): linked list problem
        # 2): Floyd's Cycle algorithm
            
        # len = n + 1
        # nums[i] in [1, n]
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

    
        