class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hs = set()
        res = 0
        
        for n in nums:
            if n in hs:
                hs.remove(n)
            else:
                hs.add(n)
                
        for i in hs:
            res = i
    
        return res
    
