# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1.val
                list1 = list1.next
            else:
                tail.next = list2.val
                list2 = list2.val

            tail = tail.next

        # list2 is empty now and we have to take remaining portion of list1 to the end
        if list1:
            tail.next = list1
        elif list2: 
            tail.next = list2       

        return dummy.next
