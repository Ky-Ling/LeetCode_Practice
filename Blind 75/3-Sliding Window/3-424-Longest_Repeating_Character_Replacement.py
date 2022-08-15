class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(26 * n) = O(n)
        
        # Count the occurrences of each character
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # The number of replacement that we need to do(The length of the window and minus
            #   the most frequency character)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res 

s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("AABABBA", 2))


        
