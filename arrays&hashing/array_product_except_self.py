class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # making preset prefix and postfix multiplication in the array
        # Question states output array is not counted towards space complexity so storing prefix in the output
        # multiply the prefixes by the current number in the input array 
        # now runthrough the output array with the postfixes multiplying to the output array, updating the postfix every time

        result = [1] * (len(nums)) #no extra memory
        
        prefix = 1 

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 
        for i in range(len(nums)- 1 , -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
            

        
