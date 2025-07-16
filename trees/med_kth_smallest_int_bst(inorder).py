# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 
        stack = []

        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur) #cross off cur
                cur = cur.left # keep moving left if not null

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val #this will always exist
            cur = cur.right
