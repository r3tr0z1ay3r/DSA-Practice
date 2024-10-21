"""
Problem:
    Given two string s1 and s2, Return true if a permutation of s1 exists in s2
    Return False if not, both contains only lowercase letters

Approach:
    Create a list of s1 values,
    Move left and right pointer when value not in s2, match check occurs in right pointer,
    When left lands at matching value, move right pointer alone, check match again
    if match continue moving right until either list is empty or mismatch occurs,
    During the match moving right,remove the list element and add to removed list using extend function,
    Once we run out of list element , return True
    If mismatch occurs move the left pointer to right pointer position
    And add the removed list elements back to the s1 list
    If right pointer reaches the end , return False

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        