class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  Hashmap - creating a dictionary - 1 HM for each word
        # Hashmap time -> O(n)
        if len(s) != len(t): # if not equal length then can't be anagram
            return False

        countS, countT = {}, {} #HM initialization

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is default if there is no key for the character (ie has 0)
            # this counts the occurances of characters with this, character may need to be initialized
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:# for keys check comparison between the two maps
            if countS[c] != countT.get(c,0):
                return False
        return True  


        # what if we  want O(1)? By sorting
        # if characters are sorted they would become the same string!
        # if interview doesn't consider sorting in the time complexity this would be the best ans in O(1)
        return sorted(s) == sorted(t)
