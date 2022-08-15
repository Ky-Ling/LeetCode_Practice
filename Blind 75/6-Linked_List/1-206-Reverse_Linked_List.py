from math import nextafter
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # (1): Iterative method
        # if not head:
        #     return None
        
        # prev, current = None, head

        # while current:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next

        # return prev

        
        # (2): Recursive method
        if not head:
            return None

        newHead = head

        if newHead.next:
            newHead = self.reverseList(newHead.next)

            head.next.next = head

        head.next = None

        return newHead


        # (3): Using stack
        if not head:
            return
        
        stack, temp = [], head

        while head:
            stack.append(temp)
            temp = temp.next
        
        head = temp = stack.pop()

        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next

        temp.next = None
        
        return None

s = Solution()
print(s.reverseList([1,2,3,4,5]))