
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:

            # Check in the hashMap to see if it is a close parentheses
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False


s = Solution()

print(s.isValid("()[]{}"))
print(s.isValid("()"))
print(s.isValid("[]"))
print(s.isValid("{}"))
print(s.isValid("{}[(])"))

