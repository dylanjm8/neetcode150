class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # .sort function
        print(nums)

        for n in range(1, len(nums)): # for each num in list
            if nums[n] == nums[n-1]: # compare to adjacent since sorted
                return True
        return False 
