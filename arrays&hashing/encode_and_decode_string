class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s # we want the result of string length to be given back in a string since its going back into the original string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j]) # will read the converted int in front of # to see how many chars have to be read to complete the string
            res.append(s[j + 1 : j + 1 + length]) # reading the length of the entire string and adding it to the list result
            i = j + 1 + length # updating the positioning of i pointer to read the next string
        return res
