# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # where s is the main tree and t is the subtree
        if not t:
            return True
        # Indicating that t exists and s doesnt
        if not s: 
            return False
        if self.sameTree(s,t):
            return True
        # recursive so keeps running 
        return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))
    def sameTree(self, s, t): # Previous Problem
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        # In the case that one is empty and another is non empty (remainder case)
        return False 
