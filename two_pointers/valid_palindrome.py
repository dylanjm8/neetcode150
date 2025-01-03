# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""

#         for c in s:
#             if c.isalnum(): # if alphanumeric (no spaces)
#                 newStr += c.lower() # add the lowercase version to the string 
#         return newStr == newStr[::-1] # ::-1 reverses the string

        # This is the cheating was using extra memory for new strings and alphanum function
# now with O(1) no extra memory no new version of the string USING POINTERS
# using ASCII instead of if alphanum, still O(n) time but O(1) memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 # pointers at start end of string (l and r) 

        while left<right:
            while left < right and not self.alphanum(s[left]): # calls another funtion inside of this same object class
                left += 1 # if not alphanumeric then move right
            while right > left and not self.alphanum(s[right]): # using while loops to ensure that the character skip is repeted as needed
                right -= 1 # if not alphanumeric then move left
            if s[left].lower() != s[right].lower(): # compare the two 
                return False
            left, right = left + 1, right - 1 # iteration after every comparison
        return True
        

    def alphanum(self, c): # the ord function coverts chars to ascii
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9')) 
# this function returns true if alphanum
