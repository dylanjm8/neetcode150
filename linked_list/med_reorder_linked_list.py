# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # order -> beggining, end, beggining, end
        # modifying in place , no extra space, constant time
        # use fast and slow pointer to determine halfway of list
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next # slow has to end up in the middle of the list by following behind
        prev = slow.next = None # split location, previous is also null for second half of list
        
        while second: # while second half exists
            tmp = second.next # reversing order of second half 
            second.next = prev
            prev = second
            second = tmp
        
        # merging the two halfs , merge to first list

        first, second = head, prev

        # first -> [1 -> 2 -> 3] second -> [6 -> 5 -> 4]
        while second:
            tmp1 = first.next # 2
            tmp2 = second.next # 5
            first.next = second # 1 -> 6 ie. pointer after first.head is going to second, these are the first two nums in list
            second.next = tmp1 # 6 -> 2
            first = tmp1 # 2
            second = tmp2 # 5

        # first -> [1 -> 6 -> 2 -> 3] second -> [6 -> 2 -> 4]

            
        
