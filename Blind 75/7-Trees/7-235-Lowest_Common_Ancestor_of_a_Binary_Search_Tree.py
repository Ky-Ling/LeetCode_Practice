# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(logn) Memory: O(1)

        if not root:
            return 

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
