# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # (1): Recursive in-order traversal --> Time and Memory: O(n)
        
        # def inorder(root: TreeNode | None) -> List[int]:
        #     return inorder[root.left] + [root.val] + inorder[root.right] if root else []

        # return inorder[root][k - 1]
 

        # (2): Iterative --> stack
        # The number of elements that we visited from our tree

        n = 0
        stack = []
        curr = root

        while curr and stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            # When the while loop is finished, means we meet None node
            # Now we have to pop out the last element that we added to the stack
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            # Go the right subtree
            curr = curr.right


    