# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # floyd's tortoise and hare algorithm O(1) slow and fast pointer
        # getting to null determines if there is no cycle
        # adding node to a hash set as 'visited' O(n) (other option)

        # fast pointer shifts by two, while slow shifts once
        # eventually the fast pointer will catch up if there is a loop

        slow, fast = head, head
        
        while fast and fast.next: # if fast made it to null it wouldn't exist, slow is irrelivent
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


