class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while (l <= r):

            mid = (l+r) // 2
            if (target == nums[mid]):
                return mid
            if (nums[l] <= nums[mid]):
                if (target > nums[mid] or target < nums[l]): # if its not in the left half
                    l = mid + 1
                else: # if it is in the left half
                    r = mid  - 1
            # right sorted portion 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
   
        return -1

            # elif(nums[mid]< target < nums[l]):
            #     l = mid + 1

    
