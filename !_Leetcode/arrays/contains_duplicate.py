class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset stores unique elements, dict(hashmap) stores key-value pairs 
        
        hs = set() # or {} but the curly braces must be filled to be a hs, or else its a dict (hm)
        
        if not nums:
            return True
        
        for n in nums: # not an index, but the actual value
            if n in hs:
                return True
            hs.add(n)
        return False
 
