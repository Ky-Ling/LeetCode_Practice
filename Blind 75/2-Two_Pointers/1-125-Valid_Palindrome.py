class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # (1): Time and memory: O(n)  
        # Removing all the non-alphanumeric characters from the input string

        # newString = ""

        # for c in s:
        #     if c.isalnum():
        #         newString += c.lower()

        # return newString == newString[::-1]


        # (2): Time: O(n) Memory: O(1)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanums(s[l]):
                l += 1

            while r > l and not self.alphanums(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r + 1

        return True


    def alphanums(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0" <= ord(c) <= ord("9"))
            )


s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(""))