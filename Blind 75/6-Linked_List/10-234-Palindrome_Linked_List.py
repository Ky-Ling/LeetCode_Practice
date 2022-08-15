# Definition for singly-linked list.
from typing import Optional

from requests import head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Two pointers: Fast and Slow

        if not head:
            return True

        fast, slow = head, head

        # Find the middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half of the linked list
        prev = None

        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # Check palindrome

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

s = Solution()

head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
head2 = ListNode(1, ListNode(2))
# print(s.isPalindrome(head1))
# print(s.isPalindrome(head2))
assert(s.isPalindrome(head1) == False)