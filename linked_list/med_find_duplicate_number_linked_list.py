class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0 , 0 # no .next? not defined above
        
        while True:
            slow = nums[slow] # move 1, since nums[slow] == 1 then slow becomes 1, and so on
            fast = nums[nums[fast]] # recursive move 2, .next.next
            if slow == fast: 
                break
            

        slow2 = 0
        
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        
        # We used floyd's algorithm to find a cycle using pointers in place without array modification
        # assuming that each val in each index points to that perticular index based on the nature of the question
