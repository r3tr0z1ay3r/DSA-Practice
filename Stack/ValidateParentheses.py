#Divide the string into two and stack em up and pop from both to check if u get valid parenthesis


class Solution:
    def isValid(self, s: str) -> bool:
        stack_simple,stack_curly,stack_square = [],[],[]
        for i in s:
            if i == "(" or ")":
                if len(stack_simple) == 2:
                    stack_simple = []
                else:
                    stack_simple.insert(0,i)
            if i == "[" or "]":
                if len(stack_square) == 2:
                    stack_square = []
                else:
                    stack_square.insert(0,i)
            if i == "{" or "}":
                if len(stack_curly) == 2:
                    stack_curly = []
                else:
                    stack_curly.insert(0,i)
            print(stack_simple,stack_curly,stack_square)
        if len(stack_square) == 0 and len(stack_curly) == 0 and len(stack_curly) == 0:
            return True
        else:
            return False
s1 = "[(])"
s2 = "([{}])"
s3="()[]{}"
obj = Solution()
print(obj.isValid(s2))