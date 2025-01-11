class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need a linear time O(n) solution since the exponential runs out of time
        # want to move the lowest pointer towards the centre
        # store the highest current area
        res = 0
        l = 0
        r = len(heights) - 1

        while (l < r):
            area = (r - l) * min(heights[l], heights[r]) # compute area by multiplying the width (difference) and the smallest bar of each end
            res = max(res, area)
            print(area)
            if heights[l] < heights[r]:
                l += 1 # moving towards centre when left low
            else:
                r -= 1 # otherwise move the right towards the middle

        return res
                
