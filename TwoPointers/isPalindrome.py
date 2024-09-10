class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [str.lower() for str in s if str.isalpha() or str.isdigit()]
        print(s)
        l,r = 0,len(s)-1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
obj = Solution()
s = "Was it a car or a cat I saw?"
print(obj.isPalindrome(s))