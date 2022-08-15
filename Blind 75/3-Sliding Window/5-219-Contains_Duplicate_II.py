from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
                
        # return False

        count = set()
        l = 0
        
        for r in range(len(nums)):
            while nums[r] in count:
                if abs(l - r) <= k:
                    return True
                else:
                    count.remove(nums[l])
                    l += 1
            else:
                count.add(nums[r])
        return False

s = Solution()

print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))