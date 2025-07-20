class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # follow up : O(1) space O(n) time -> bit manipulation
        # XOR [0,1]

        res = 0
        # index vs count of items in array, how to access count?
        for i,n in enumerate(nums):
            res ^= (i+1)
        print(res)
        # going back through the array and XOR with values gives the remaining that doesnt exist in the input
        for n in nums:
            res ^= n 
        return res
        # hs = set(nums)

        # for i in range(0,len(nums)):
        #     if i not in hs:
        #         return i

        # return len(nums)

            
