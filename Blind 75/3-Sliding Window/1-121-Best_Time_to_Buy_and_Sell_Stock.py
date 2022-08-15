from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Memory: O(1)
        
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

            else:
                l = r
            r += 1

        return maxProfit



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))




    