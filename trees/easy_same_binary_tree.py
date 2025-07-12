# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Cases
        if not p and not q: # if both trees are now empty, return True 
            return True

        if not p or not q or p.val != q.val: # if values of the trees are different or only one tree doesn't exist then return false
            return False

        
        # using dfs recursion
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False 
        

