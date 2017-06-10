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
    
    #case 1
    if len(p) == 1 or p[1] != '*':
        #if the length of s is 0, return false
        if len(s) < 1:
            return False
        #if the first does not match, return false
        elif p[0] != '*' and s[0] != p[0] and p[0]!='.':
            return False
        #otherwise, compare the rest of the string of s and p.
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
        

def regularExpressionMatchingDP(s, p):
'''
reference: https://discuss.leetcode.com/topic/40371/easy-dp-java-solution-with-detailed-explanation
1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
'''
    dp = [ [False for _ in range(len(p) + 1)] for _ in range(len(s) + 1) ]
    dp[0][0] = True

    for idx, ch in enumerate(p):
        if ch == '*':
            dp[0][idx+1] = dp[0][idx-1]

    for i, sl in enumerate(s):
        for j, pl in enumerate(p):
            if dp[i][j] and (sl == pl or pl == '.'):
                dp[i+1][j+1] = dp[i][j]
            elif pl == '*':
                if s[i] == p[j-1] or p[j-1] == '.':
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j-1]
                    
    return dp[-1][-1]
        


            
