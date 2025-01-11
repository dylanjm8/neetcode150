class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums): # iterating over the index and values of the list through enumerate
            if i > 0 and a == nums[i-1]: 
                continue # eliminating the usage of repeat numbers

                l = i + 1
                r = len(nums) - 1

                while l < r:
                    threeSum = a + nums[l] + nums[r]

                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else: 
                        res.append([a, nums[l], nums[r]])
                        l += 1 # move the left pointer to create a new sum
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        return res
