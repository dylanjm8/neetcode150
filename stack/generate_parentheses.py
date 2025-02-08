class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only regular parenthesis, n = pairs of parenthesis
        # close <= open ie if n = 3 then max open and close is 3

        stack = []

        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack)) # store the contents of stack in result stack using .join
                return 

            if openN < n:
                stack.append("(") 
                backtrack(openN + 1, closedN) # recursive call with an increased open bracket
                stack.pop()

            if closedN < openN:
                # We can add a closed parenthesis onto the stack if less than the open count
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        # call our second backtrack function with initial brackets of 0
        backtrack(0,0)
        return result
