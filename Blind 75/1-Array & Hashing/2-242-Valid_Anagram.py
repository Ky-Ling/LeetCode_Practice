class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # (1): O(n) O(1)
        # return sorted(s) == sorted(t)

        # (2): O(n) O(n)
  
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True



s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("cas", "acs"))
print(s.isAnagram("cas", "ass"))
