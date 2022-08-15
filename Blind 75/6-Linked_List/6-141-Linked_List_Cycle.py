# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # (1):
        # hashSet = set()
                
        # if not head:
        #     return 
        
        # while head:
        #     if head.next in hashSet:
        #         return True
        #     hashSet.add(head)
        #     head = head.next

        # return False 

        

        # (2): O(n)
        if not head:
            return 

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False



