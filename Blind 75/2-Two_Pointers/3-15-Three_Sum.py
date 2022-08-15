import enum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # (1): Brute force: Time: O(n ^ 2), Space: O(n)

        # def two_sum(index):
        #     target_sum = -nums[index]
        #     left, right = index + 1, len(nums) - 1

        #     while left < right:
        #         current_sum = nums[left] + nums[right]

        #         if current_sum < target_sum or (left > index + 1 and nums[left] == nums[left - 1]):
        #             left += 1

        #         elif current_sum > target_sum or (right < len(nums) - 2 and nums[right] == nums[right - 1]):
        #             right -= 1 

        #         else:
        #             res.append([nums[index], nums[left], nums[right]])
        #             left += 1


        # res = []
        # nums.sort()

        # for i in range(len(nums)):
        #     if i == 0 or (nums[i - 1] != nums[i] and nums[i] <= 0):
        #         two_sum(i)

        # return res



        # (2): Time: O(nlogn) + O(n ^ 2) = O(n ^ 2)
        # Space: O(1) or O(n) Depending on the sorting algorithm we are using

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1

                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])

                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        l += 1

        return res



s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0]))
print(s.threeSum([]))




    