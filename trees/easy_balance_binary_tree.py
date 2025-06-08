# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root) ->  [bool,int]: # nested funtion allows to return multiple values instead of just boolean
            if not root: # if tree is empty it is balanced 
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right) # recursive call for tree branches left and right


            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # left and right subtrees have to return true for balance 
            return [isBalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
