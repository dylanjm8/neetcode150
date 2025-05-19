# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# singly linked list 

# class ListNode: 
    # def __init__(self, val = 0, next = None):
    #     self.val = val
    #     self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # given singly linked list 
        # using two pointers, prev, curr
        # time O(n) -> pointers
        # involves flipping pointing direction for list
        # Previous becomes new head of linked list 

        prev , curr  = None, head 
        
        while curr:
            nxt = curr.next # saving the next node before updating it to previous
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
