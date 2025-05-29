class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1

        while r >= l:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            mid = (l+r) // 2 # if r = l, this just gives us their indicies
            res = min(res,nums[mid])
            if (nums[mid] < nums[l]):
                r = mid - 1
            else:
                l = mid + 1
            
        return res

