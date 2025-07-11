class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)
        print(res)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res
        # arr = [0, len(nums) - 1]


        
