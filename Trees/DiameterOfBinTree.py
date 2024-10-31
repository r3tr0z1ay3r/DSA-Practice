"""
Intiution:
    Perform dfs while updating result of the diameter

Approach:
    We maintain a result variable which will be updated while we perform dfs
    A nested function dfs will iterate through the tree
    At each point it will update the result with the diamter
    And also update the height of the current dfs
    At the end we return the result variable

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res,left+right) #Getting the diameter of the tree at this level
            return 1 + max(left,right) #Return case for the recursive dfs returing the height
        return res
