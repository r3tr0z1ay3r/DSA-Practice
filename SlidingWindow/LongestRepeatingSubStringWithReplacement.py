"""
Prblm:
Given a string "s" and int "k", from the string "s" we can change "k" chars,
after performing atmost k replacement, find the longest substring with only one distinct char

Approach - 1(Solution):
Use a left pointer and right pointer ,
Move the right pointer as long the letter is the same, or replacement is allowed,
Move the left pointer when it is a different letter or no more replacement allowed.
Update the value by comparing current max and old max

Acutal Solution:
Maintain a hashmap, This acts as the window holding (Letter,Appearance of letter in the window)
Left pointer is intialized at 0 and right pointer is mainted by for loop till the length of the string

We maintain a check condition which checks if replacement is allowed:
If replacement is allowed then we simply move the right pointer
If replacement is not allowed we do two changes:
Decrease the count of letter at left pointer by 1 in the hash map
Move the left pointer , i.e increase left by 1

At the end of this iteration we will return the lenght of the window
which is the length between the left and right pointer
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        replacement = k
        left,right = 0,1
        res,repeat = 0,0
        while right < len(s)-1:
            if s[left] == s[right] and replacement != 0:
                right += 1
                print("Moving Right",s[right])
            elif s[left] != s[right] and replacement !=0:
                replacement -= 1
                right += 1
                print("Moving Right with replacement",s[left])
            else:
                left += 1
                replacement = k
                print("Moving left and refreshing replacement")
            print(f"Current Substring {s[left:right]}")
            res = max(len(s)-right,res)
        print(res)


class ActualSolution:
    def characterReplacement(self,s:str,k:int):
        count = {}
        l,mostFreq = 0,0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) #Get the rth pointer letter and increase its count by 1,0 if doesnt exists
            mostFreq = max(mostFreq,count[s[r]])
            if (r-l)-mostFreq >= k:  #(r-l) gives the size of window
                count[s[l]] -= 1 #Since window does not have left value, decrement the left val count
                l += 1 #Move left pointer

        return (r-l) + 1
        
obj = Solution()
s1,k1 = "XYYX", 2 #output :4 
s2,k2 = "AAABABB", 1 #Output : 5

characterReplacement(s2,k2)
#obj.characterReplacement(s=s1,k=k1)
#obj.characterReplacement(s=s2,k=k2)


