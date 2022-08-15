# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If the subRoot tree is empty, it will be a subtree of other tree regardless of whether
        #   the other tree is empty or not.
        if not root:
            return False
        
        if not subRoot:
            return True

        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and (self.isSameTree(root.right, subRoot.right)))

        return False