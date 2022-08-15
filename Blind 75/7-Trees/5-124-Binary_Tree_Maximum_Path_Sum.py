from typing import Optional


# (1): 

class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    max_sum = float("-inf")

    def max_path_sum_ending_with_node(node: Node):
        nonlocal max_sum

        if not root:
            return 0

        left_path_sum = max(0, max_path_sum_ending_with_node(node.left))
        right_path_sum = max(0, max_path_sum_ending_with_node(node.right))

        path_sum_with_node = node.val + left_path_sum + right_path_sum
        max_sum = max(max_sum, path_sum_with_node)

        return node.val + max(left_path_sum, right_path_sum)

    max_path_sum_ending_with_node(root)

    return max_sum


root1 = Node(1, Node(2, Node(4), Node(5)), Node(
    3, Node(6, Node(8)), Node(7, None, Node(9))))

expected = 33
actual = max_path_sum(root1)

print(expected == actual)



# (2): 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # O(n) and O(logn)
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]

            
