"""
Intiution:
    Iterate thro each child until Leaf
    return the max val

Approach:
    Using recursion we will dive down each level of each child,
    at each level we will add 1 to its value starting from 0 on the bottom (Recursion return case)
    By adding it up from bottom to top(Recursion), we will get the max val

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        left_val = 0
        right_val = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxVal = 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        return maxVal
