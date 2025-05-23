"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None} # For edge case we want a null to map to null

        curr = head # define linked list head from passed in
        # First pass for nodes
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy # mapping, as curr increases (curr is just a value of index), then the copies are filled to the corresponding indicies
            curr = curr.next

        curr = head 
        # Second pass for pointers
        while curr: # even though it looks like only copy is updated it is actually a complete copy of the dictionary, and allows for updating within the list
            copy = oldToCopy[curr] # set copy to the copy we made in the first pass (oldToCopy is a copy) as we set above, matching copy to oldToCopy
            # KEY: by setting copy = oldToCopy[curr] we are modifying and making changes using copy that edits into the dictionary
            copy.next = oldToCopy[curr.next] # setting the copy.next to be the same as the previous curr.next
            copy.random = oldToCopy[curr.random] # same for random, these three lines are doing the same thing just for all atributes of the nodes
            curr = curr.next # iteration 

        return oldToCopy[head] # return the head as passed in to function 
            
