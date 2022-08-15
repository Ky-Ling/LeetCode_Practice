from calendar import c
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # (1): Brute force: O(m ^ n)
        # (2): Binary Search : O(m ^ logn)
        # (3): But we can run binary search on each row to find out which row the target is at.
        #   --> O(logm + logn)
        
        # (1):
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False


        # (2): 
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            
            while l <= r:
                mid = int(l + ((r - l) // 2))
                if target == matrix[i][mid]:
                    return True

                elif target < matrix[i][mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False



        # (3): 
        # ROWS, COLUMNS = 0, len(matrix[0])
        # top, bottom = 0, ROWS - 1

        # while top <= bottom:
        #     middle_row = (top + bottom) // 2

        #     if target < matrix[middle_row][0]:
        #         bottom = middle_row - 1
        #     elif target > matrix[middle_row][-1]:
        #         top = middle_row + 1
        #     else:
        #         break
        
        # if not(top <= bottom):
        #     return False
        
        # current_row = middle_row
        # l, r = 0, COLUMNS - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if target < matrix[current_row][mid]:
        #         r = mid - 1
        #     elif target > matrix[current_row][mid]:
        #         l = mid + 1
        #     else:
        #         return True
        # return False



s = Solution()

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20))
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
