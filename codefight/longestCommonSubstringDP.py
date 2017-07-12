def longestCommonSubstring(s, t):
    if len(s) == 1:
        return 1 if s in t else 0
    if len(t) == 1:
        return 1 if t in s else 0
    l = 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    maxlen = 0
    for i in range(len(t)):
        for j in range(len(s)):
            if  t[i] != s[j]:
                dp[i][j] = 0
            else:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i-1][j-1]
                if maxlen < dp[i][j]: maxlen = dp[i][j]
    return maxlen
        
