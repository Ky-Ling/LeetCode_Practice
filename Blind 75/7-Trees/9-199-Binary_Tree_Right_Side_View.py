# Definition for a binary tree node.

import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSideElement = None
            qLength = len(q)

            for _ in range(qLength):
                node = q.popleft()

                if node:
                    rightSideElement = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSideElement:
                res.append(rightSideElement.val)

        return res