"""
intution:
    Move left and right pointer till we hit a char in set,
    Move right till all chars matches, Reset right to left position and move again
    Append each subset to list and return smallest

approach:
    create a hash of "t" with each having 1
    move the pointer while creating a window hash (elm:count) of current elms
    compare the hash of t's value with window's key value if any,
    if >= 1 for all, add current window to list,and reset right to left position
    if not keep moving right
    repeat

    In the list of all subsets,get the lowest size elm

Actual Approach:
    Create hash of t elms with thier count,
    We use sliding window approach to find subsets that satisfy thier condition
    At each step we create a hash of window (char:count)
    Create and maintain an have and need value comparing hash of current window and hashed t
    Also create a dummy result value and result length, ensuring that we get the proper result

    We check if the current char exists in the hashed t and if the hashvalue of char are same in window and hashed t
    if they are same then we increase the have by 1

    We also create a loop when have and need are the same (Valid subset)
    we find the length of the current window by (r - l + 1) ,
    if lower than resLen , we update the res and resLen
    In the loop we pop the left elements of the window and updating its value in the window hash and do a check condition

    In this check condition we check if the popped left elm in the t and if its hash value is lower than hashed t
    if so then we decrement have by 1
    At the end of the loop we increase the left pointer by 1

    In the end we get the res val having the positions of the smallest subset
    return the substring if it exists
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        count_T,window = {},{}
        for i in t:
            count_T[t] = 1 + count_T.get(i,0)
        have,need = 0,len(count_T)
        l = 0
        res,resLen = [-1,-1],float("infinity") #res is the string and resLen is the length of res
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char,0)
            if char in count_T and window[char] == count_T[char]:
                have += 1
            while have == need:
                if (r-l + 1) <= resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
            l += 1
        l,r = res
        return s[l:r +1] if resLen != float("infinity") else ""
obj = Solution()
s1,t1 = "ADOBECODEBANC","ABC"
s2,t2 = "OUZODYXAZV","XYZ"

obj.minWindow(s2,t2)
                