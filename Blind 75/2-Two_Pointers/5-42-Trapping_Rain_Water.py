from turtle import right
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # For every index i, we have to count maxLeft, maxRight, min(maxLeft, maxRight)
        #   We have to make sure that min(maxLeft, maxRight) - height[i]>= 0
        
        # (1): Time: O(n) Memory: O(n)
        #  --> Create new array to store these information
        
        # (2): Time: O(n) Memory: O(1)
        #    Two pointers
        
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))


