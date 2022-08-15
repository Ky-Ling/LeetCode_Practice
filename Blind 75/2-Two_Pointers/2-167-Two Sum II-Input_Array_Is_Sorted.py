from operator import le
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # (1): Brute force: O(n ^ 2)
        # for i in range(len(numbers) - 1):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]


        # (2): Two pointers: O(n)
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                return [left + 1, right + 1]
            
        return []


s = Solution()

print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2, 4, 5], 7))
print(s.twoSum([-1, 3, 1, 5], 8))
print(s.twoSum([-1, 3, 1, 5], 2))
