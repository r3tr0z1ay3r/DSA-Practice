"""
Prblm:
 Given two trees, return True if they are the same or return False
 Each node should have the same left and right and the same value

Intiution:
    Using recursion on dfs, we can find out if they values are the same

Approach:
    The base case:
        if both the tree are at the bottom (both None) return True
    Recursion case:
        Check if both the p and q are True,if so check if they have the same value
        at each stage return the left node and right node dfs-wise
        if it fails at any stage it returns False
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False