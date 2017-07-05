'''
ref: https://codefights.com/interview-practice/task/C8Jdyk3ybixqQdAvM/description

Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

Example

For s = "CodefightsIsAwesome" and x = "IA", the output should be
strstr(s, x) = -1;
For s = "CodefightsIsAwesome" and x = "IsA", the output should be
strstr(s, x) = 10.
'''

def findFirstSubstringOccurrence(haystack, needle):
    if len(needle)==0:
        return haystack
    table = [0] * len(needle)
    j, i = 0, 1
    while i < len(needle):
        if needle[i] != needle[j]:
            if j > 0:
                j = table[j-1]
            else:
                i += 1
        else:
            table[i] = j + 1
            i += 1
            j += 1
    
    m, i = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[m]:
            if m == len(needle) - 1:
                return i - len(needle) + 1
            else:
                m += 1
                i += 1
        else:
            if m == 0:
                i += 1
            else:
                m = table[m-1]
    return -1
