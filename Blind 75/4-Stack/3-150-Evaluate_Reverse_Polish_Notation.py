from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(c))

        return stack[0]


s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
