"""
Prblm:
Given a string with various characters, find the longest substring(continous chars) with no duplicates and return its values,
there can be empty strings which should be considered for edge cases,

Approach:
-> Own
    if the length of the string is 0 we return 0 as there can be no vals from it,
    we intialize a arr for maintaining all the seen values and a value to maitain the current largest no,
    we iterate through the loop comparing with the next elm and that if they are on the seen list,
    if not we append the val to the seen array while updating the current value and comparing it with the current max and update if neseccary,
    if it is unable to satisfy that condition we simply reset the curr pointer and loop through it,

    Issues faced:
        Since we are comparing the next elm, nearing the end of the string we are unable to properly process the values
        resulting in incorrect values.
->Given
    We initalize a set of chars holding the non duplicate values in them,we iterate through the value and add those values to the char set,
    if there are values in the char set then we remove them and and the l val by 1,
    at the end of each iteration we update the largest value if neseccary

"""


class Solution:
    def lengthOfLongestSubstringOWN(self, s: str) -> int:
        if len(s) == 0:
            return 0
        largestCount = 1
        curr = 0
        seen = []
        for i in range(len(s)-1):
            print(seen)
            print(s[i],s[i+1])
            if s[i] != s[i+1] and not (s[i] in seen):
                print("In if statement")
                curr += 1
                seen.append(s[i])
                largestCount = max(largestCount,curr)
            else:
                curr = 0
        print(largestCount)
        return largestCount

    def lengthOfLongestSubstring(self,s:str) -> int:
        maxVal = 0
        l = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxVal = max(maxVal,r-l+1)
        print(maxVal)

obj = Solution()
string = "zxyzxyz"
string2 = "xxxx"
string3 = "au"
obj.lengthOfLongestSubstring(string)

