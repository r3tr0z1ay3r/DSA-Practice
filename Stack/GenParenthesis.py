from itertools import permutations as pm
def isValid( s) -> bool:
    if len(s) % 2 != 0:
        return False
    else:
        stack = []
        hash_close = {"]":"[",")":"(","}":"{"}
        for char in s:
            print(stack)
            if char in hash_close.keys() and len(stack) != 0:
                if hash_close[char] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
    
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        p_list = "()"*n
        for i in pm(p_list):
            if isValid(i):
                print(i)

obj = Solution()
obj.generateParenthesis(3)