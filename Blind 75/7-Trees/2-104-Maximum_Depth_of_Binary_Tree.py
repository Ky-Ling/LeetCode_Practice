# Definition for a binary tree node.
from logging import _Level
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # (1): Recursive DFS --> Time and memory: O(n)
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # (2): BFS ->  Time and Memory: O(n)

        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:

            # Get through the queue and remove the element that currently in it
            # Remove all the element and add the children
            # Traversal the entire level and add the next level. While we finish the loop,
            #   we have the increase the level
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level

        
        # (3): Iterative DFS

        stack = [root, 1]
        res = 0

        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)

                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res

