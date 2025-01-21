class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1count = [0] * 26 # lists are initialized since there is no need for key value
            # the first list is compared to the second list so the positions of characters is irrelevent

        s2count = [0] * 26

        for i in range (len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1 # converts the string value to an ascii number relative to the lowercased alphabet 
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0
            
        for i in range (26): #parses the hashmaps
            matches += (1 if s1count[i] == s2count[i] else 0 )

        l = 0  

        for r in range(len(s1), len(s2)): # iterates starting at the end of the length of the first string to the end of the compared second string (using right pointer)
            if matches == 26:
                return True 

            # increments at right pointer for character being added
            index = ord(s2[r]) - ord('a') # getting index since list was used instead of hashmap
            s2count[index] += 1 # increases the count of the corresponding character from string s1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            # Left pointer (decrement count at left pointer location since it is leaving the window)
            index = ord(s2[l]) - ord('a') # getting index since list was used instead of hashmap
            s2count[index] -= 1 # increases the count of the corresponding character from string s1
            if s1count[index] == s2count[index]: # if counts are NOW equal (regardless of increment or decrement)
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        return matches == 26# accounts for the last iteration case if the character count is exact then true will be returned

            
