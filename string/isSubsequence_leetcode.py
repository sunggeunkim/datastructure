'''
reference: https://leetcode.com/problems/is-subsequence/#/description
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "": return True
        if t == "": return False
        j = 0
        for i in range(len(t)):            
            if t[i] == s[j]:
                j += 1
            if j == len(s): return True
        return False
    
'''Efficient Solution:

from collections import defaultdict
from bisect import bisect_left
class Solution(object):
    
    def createMap(self, s):
        # create a map. key is char. value is index of apperance in acending order. 
        posMap = defaultdict(list)
        for i, char in enumerate(s):
            posMap[char].append(i)
        return posMap
        
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        posMap = self.createMap(t)
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True
 '''
