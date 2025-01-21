class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #create hash map
        res = 0

        l = 0
        
        for r in range(len(s)): # run until right pointer reaches the end
            count[s[r]] = 1 + count.get(s[r], 0) # update the count hash map with the character under the right pointer  
            # count[s[r]] is the value assosiate with the key at the index s[r]
            while (r-l + 1) - max(count.values()) > k: # length of window - the count of most frequent value is more than k (can't be replaced)
                count[s[l]] -= 1
                l += 1 # move the widow and decrement the value thats removed from the window

            res = max(res, r-l + 1) # update the result if a valid window is found
        return res
