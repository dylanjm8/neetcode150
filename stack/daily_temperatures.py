class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # days away from next warmer temp (essentially difference in stack), if none fill 0
        # monotonic (decreasing) (or equal) stack 

        tempStack = [] # also includes index [temp, index]
        
        res = [0] * len(temperatures) # Will be a zero if not changed

        for i, t in enumerate(temperatures): # we want the index and value , since we have to compare positions in the array
            while tempStack and t > tempStack[-1][0]: # [-1] is top of temp stack, so if the stack exists and the new temp is greater than the previous
                stackT, stackInd = tempStack.pop()
                res[stackInd] =  (i - stackInd)     
            tempStack.append([t,i])
        return res
