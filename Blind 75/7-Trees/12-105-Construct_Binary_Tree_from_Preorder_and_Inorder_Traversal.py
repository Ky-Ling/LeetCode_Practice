# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
    The first value of the pre-order traversal is always going to be the root.
    
    When we remove the root value from the pro-order traversal list, we have to go to in-order
    traversal list, and we can notice that the values of left side of the root value are the left subtree,  every value to the right of the root value will go to the right subtree.
    
    And we can get the length of the left and right subtrees and it will tell us how to partition
    the pre-order traversal. And then recursively call and function to create the left and right
    subtrees.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        # Find the position of root in the in-order list
        mid = inorder.index(preorder[0])

        # Create the left and right subtree recursively 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root