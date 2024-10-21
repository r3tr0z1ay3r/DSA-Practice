"""
Problem:
    Given two string s1 and s2, Return true if a permutation of s1 exists in s2
    Return False if not, both contains only lowercase letters

Approach(Failed):
    Create a list of s1 values,
    Move left and right pointer when value not in s2, match check occurs in right pointer,
    When left lands at matching value, move right pointer alone, check match again
    if match continue moving right until either list is empty or mismatch occurs,
    During the match moving right,remove the list element and add to removed list using extend function,
    Once we run out of list element , return True
    If mismatch occurs move the left pointer to right pointer position
    And add the removed list elements back to the s1 list
    If right pointer reaches the end , return False

Approach:
    Create a hash of s1 values and thier count,
    Create a fixed window of sizee of s1 
    Slide the window through the string s2 while creating a hash of the values in the window
    Compare the s1 hash and the current window's hash, if they are teh same return true
    Slide the window till the end of the s2, if no matches found return False

"""

class aSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s,removed = [i for i in s1],[]
        l,r = 0,0
        while r < len(s2):
            print(s2[r],r)
            if s2[r] not in s:
                print(f"Not in {s}")
                r += 1
                s.extend(removed)
                removed = []
            else:
                print("In S")
                removed.append(s2[r])
                s.remove(s2[r])
                if len(s) == 0:
                    return True
                r += 1
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_hash = {}
        for i in s1:
            s1_hash[i] = s1.count(i)
        print(s1_hash)
        l = 0
        r = len(s1)-1
        while r < len(s2):
            print("resetting window")
            window_hash = {}
            for i in range(l,r+1):
                print(f"Elm is {s2[i]}")
                window_hash[s2[i]] = 1 + window_hash.get(s2[i],0)
            print(window_hash)
            if s1_hash == window_hash:
                return True
            l += 1
            r += 1
        return False

    
s3 = "ab"
s4 = "lecabee"
s1="adc"
s2="dcda"
obj = Solution()
print(obj.checkInclusion(s3,s4))