# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        output = []
        
        if not root:
            return output

        process_queue = deque([root])

        while process_queue:
            n = len(process_queue)
            t = []

            for _ in range(n):
                node = process_queue.popleft()
                t.append(node.val)

                if node.left:
                    process_queue.append(node.left)
                
                if node.right:
                    process_queue.append(node.right)

            output.append(t)

        return output
        
