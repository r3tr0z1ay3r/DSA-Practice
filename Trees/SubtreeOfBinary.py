"""
Problem:
    Given two trees root and subroot
    Return true if subroot exists in root
    return false else

Intiution:
    Using nested dfs to find out if tree exists

Approach:
    we intialize outer dfs to iterate through the entire tree 
    while checking if the current node is the same as the subtree node
    if it is the same we start the nested dfs from this node
    if not we move the outer dfs to the next level

    we use a helper function "sameTree" to perform the nested dfs
    in set the base case to return true when we reach the end of the both tree
    at each step we check if both the root and subtree node are flagged as true and then
    we check if both the value of current root node and subroot node are the same
    if so we continue with the next level of dfs
    if not we return false

    This dfs is continued until we either reach the root of both trees and return True
    or we simply fail a case and return false



"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def sameTree(self,root,subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        return False