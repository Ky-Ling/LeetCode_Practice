import enum
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # (1): Brute force: O(n ^ 2)
        
        # (2): Monotonic stack(decreasing order)
       
        # res = [0] * len(temperatures)

        # for i in range(len(temperatures) - 1):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res
 

        # (2): 
        res = [0] * len(temperatures)

        # pair: [temp, index]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()

                res[stackIndex] = (i - stackIndex)
            
            stack.append([t, i])

        return res



s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures( [30,60,90]))