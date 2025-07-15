# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # we want to use dfs(recursive) to impliment this solution,
        # by updating bounds, we can decide validity

        def valid(node, left, right): # left and right are the boundries
            if not node:
                return True # if null tree then still valid

            if not (left < node.val < right): #conditions to satisfy
                return False

            return (valid(node.left, left, node.val) and # if moving left the upper bound must be updated
            valid(node.right, node.val, right)) # if moving right there becomes a new lower bound
            # this will return true if all left and rights are valid and false otherwise

        return valid(root, float("-inf"), float("inf")) # defining infinity bounds in python
