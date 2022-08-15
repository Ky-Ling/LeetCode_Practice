from pickletools import stackslice


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # O(n) --> Add charactor and O(n) --> Remove charactor, total: O(2n) = O(n)
        # Space: O(n)
        
        # [char, count]
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += (char * count)

        return res

    
s = Solution()
print(s.removeDuplicates("abcd", 2))
print(s.removeDuplicates("deeedbbcccbdaa", 3))
print(s.removeDuplicates("pbbcggttciiippooaais", 2))