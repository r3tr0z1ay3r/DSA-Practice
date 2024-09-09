class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack (openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closeN) #recursive call to with one more open parenthesis
                print(stack)
                stack.pop() # After recursion pop that finished brackets
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                print(stack)
                stack.pop()
        backtrack(0,0)
        return res
    
"""keep two trackers for the open parenthesis and close parenthesis
using recursion we can call on other possible decision, following the rules of recursion 
 -> Have a base class
 -> Have the problem shrink to base class"""