class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using a set for the original array , it can be parsed forward and back again easily O(n), (operation for each n in array)

        consec = set(nums)
        longest = 0 # storing the current leader for the longest consecutive numbers in the array

        
        for n in nums: # want to check array against the set which was filled
            if (n-1) not in consec:
                count = 0 
                while (n + count) in consec:
                    count += 1
                longest = max(count, longest) # we want to update the value of the longest sequence if the current count happens to be greater
        return longest

        
            
