# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy # to prevent edge cases where the list sits empty
        # assuming lists are sorted  
        while l1 and l2: # while both the input lists are not empty 
            if l1.val < l2.val: # val is the current node given class def above
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1: # one of the lists could still have numbers at the end remaining, they should be appended to tail
            tail.next = l1
        elif l2: 
            tail.next = l2
        
        return dummy.next
