# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # finding the root in inorder
        # passing in the left of preorder since the furthest left will be defined as the new root
        # passing in whatever is left of the preorder root in inorder into inorder, because this is the actual nodes left of the root
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # mid + 1 is NOT inclusive in python
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        # we are building from the root node with the above lines
        return root
