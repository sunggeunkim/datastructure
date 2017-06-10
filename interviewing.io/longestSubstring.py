# Given a string ,return the longest substring that contains at most two distinct characters.

def isAnyZero(d):
    for key in d:
        if d[key] == 0:
            del d[key]
            return True
    return False

def longest_substring(s):
    if len(s) <= 2:
        return s
    d = {s[0]:1}
    counter = 1
    left = 0
    maxlength = 0
    n = len(s)
    for right in range(1,n-1):
        if s[right] in d:
            d[s[right]] += 1
            continue
        else:
            if counter < 2:
                counter += 1
                d[s[right]] = 1
            else:
                length = right - left
                if length > maxlength:
                    maxlength = length
                    maxsubstring = s[left:right]
                zeroTrue = False
                while not zeroTrue:
                    d[s[left]] -= 1
                    left += 1
                    zeroTrue=isAnyZero(d)
                d[s[right]] = 1
    if s[n - 1] in d or counter < 2:
        length = n - left
        if length > maxlength:
            maxsubstring = s[left:]
    else:
        if maxlength == 0:
            maxlength = n - 1
            maxsubstring = s[left:n-1]
        else:
            zeroTrue = False
            while not zeroTrue:
                d[s[left]] -= 1
                left += 1
                zeroTrue = isAnyZero(d)
            if n - left > maxlength:
                maxsubstring = s[left:]        

    return maxsubstring
                



print(longest_substring("abbcc"))
print(longest_substring("ababcbcbb"))
print(longest_substring("cbbcbbbb"))
print(longest_substring("aaaaaaaa"))
print(longest_substring("a"))
print(longest_substring("aa"))
print(longest_substring("abc"))
print(longest_substring("aaaaaaaabc"))
