class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # split down middle? - binary search, l and r pointers define valid range for appearance of number

        l, r = 0, (len(nums) - 1) # r sits at end

        while l <= r:
            mid = (r + l) // 2 # could end up in overflow
            # Solution: mid = l + (r - l)//2 
            # this avoids adding the two ints together

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]: 
                r = mid - 1
            else :
                return mid
        return -1


        
