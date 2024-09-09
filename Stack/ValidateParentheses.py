class Solution:
    def isValid(self, s: str) -> bool:
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