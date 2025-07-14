# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS ALGORITHM - linear time and space

        res = [] # result array (1D!)

        q = collections.deque() #package for queues in python

        q.append(root) #start at root

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft() # popleft = remove from queue fifo
                if node:
                    level.append(node.val) # adds nodes on left first complying with fifo
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level) # appending level array to final array

        return res

