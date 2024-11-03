"""
A binary tree is heigh balanced when the height of left and right subtree difference is < 1
Return true if balanced or return false

Intituion:
    Use DFS to check if its balanced at each level and return it recursively

Approach:
    We use recursive dfs to iterate to each level,
    At each level we return a list containing two things
    [bool,int] -> bool : If the nodes visited before are balanced,
                  int : The number of sub trees at this level
    We iteratively update this value during the stage of dfs
    At the end we will return the bool to find out if the tree is balanced or not
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs (root):
            if not root: #Recursive Base Case
                return [True,0]
            left,right = dfs(root.left),dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1 #Checking if the difference between both the subtree <= 1
            return [balanced,1+max(left[1],right[1])] #Recursive Return Case

        return dfs(root)[0]