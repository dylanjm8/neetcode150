class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack is implimented as regular list/array
        closeToOpen = {")": "(", "]" : "[", "}" : "{"} #Hashmap to match key value brackets (keys are close brackets values are open)


        for c in s:
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]: # checking if the top of the stack is equal to the matching bracket in hashmap and if the stack is not empty
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        return True if not stack else False 
    
