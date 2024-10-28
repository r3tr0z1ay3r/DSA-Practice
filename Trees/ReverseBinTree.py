"""
Intiution:
    Iterate thro the tree via DFS
    Swapping the left with the right subtree
    Repeat until reversed

Approach:
    Using recursion we can implement dfs to iterate through the tree
    At each stage , we swap the left value with the right value

    And then we do a recursive call on either the left side of the tree or the right side of the tree
    This runs until we reach the leaf node of the left or right subtree 
    The stop condition will be either when the root is Null,or return the root
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root