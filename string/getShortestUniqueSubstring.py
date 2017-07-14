def getShortestUniqueSubstring(arr, s):
    arr = set(arr)
    length = len(arr)
    count = 0
    tail = 0
    minLength = len(s)
    result = ""
    dic = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in arr:
            c = dic[ch]+1 if ch in dic else 1
            if c == 1: count += 1
            dic[ch] = c
        while count == length:
            if s[tail] in arr:
                v = dic[s[tail]]
                if v - 1 == 0:
                    count -= 1
                dic[s[tail]] = v-1
            if i - tail + 1 < minLength:
                minLength = i - tail + 1
                result = s[tail:i + 1]
            tail += 1
            if (minLength == length):
	            return result
    return result

print(getShortestUniqueSubstring(['a','b','c'], 'bccaaccbbzzzac'))

