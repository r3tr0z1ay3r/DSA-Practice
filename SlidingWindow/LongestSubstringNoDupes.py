class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            print(s[i])


obj = Solution()
string = "zxyzxyz"
obj.lengthOfLongestSubstring(string)