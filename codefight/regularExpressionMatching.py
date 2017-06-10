'''
ref: http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
regularExpressionMatching(s,p)

output: boolean

Some examples:
regularExpressionMatching("aa","a") return false
regularExpressionMatching("aa","aa") return true
regularExpressionMatching("aaa","aa") return false
regularExpressionMatching("aa", "a*") return true
regularExpressionMatching("aa", ".*") return true
regularExpressionMatching("ab", ".*") return true
regularExpressionMatching("aab", "c*a*b") return true
'''

def regularExpressionMatching(s, p):
    
    #base case
    if len(p) == 0:
        return len(s) == 0
    
    #special case
    if len(p) == 1:
        #if the length of s is 0, return false
        if len(s) < 1:
            return False
        #if the first does not match, return false
        elif p[0] != '*' and s[0] != p[0] and p[0]!='.':
            return False
        #otherwise, compare the rest of the string of s and p.
        else:
            return regularExpressionMatching(s[1:], p[1:])
        
    #case 1: when the second char of p is not '*'
    if p[1] != '*':
        if len(s) < 1:
            return False
        if p[0] != s[0] and p[0] != '.':
            return False
        else:
            return regularExpressionMatching(s[1:], p[1:])
        
    #case 2: when the second char of p is '*', complex case.
    else:
        
        # case 2.1: a char & '*' can stand for 0 element
        if regularExpressionMatching(s, p[2:]):
            return True
        
        #case 2.2: a char & '*' can stand for 1 or more preceding element, 
		#so try every sub string
        i = 0
        while i < len(s) and (s[i] == p[0] or p[0] == '.'):
            if regularExpressionMatching(s[i+1:], p[2:]):
                return True
            i += 1
            
        return False
        


            
