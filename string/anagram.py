'''
Given two strings, write a function to determine whether they are anagrams.

abcde
edcba
-> True
'''

def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    d = {}
    for c in str1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in str2:
        if c not in d:
            return False
        if d[c] == 0:
            return False
        d[c] -= 1

    for key in d:
        if d[key] != 0:
            return False
    return True

print(is_anagram('abcde','egdbac'))
print(is_anagram('',''))
print(is_anagram('a','a'))
print(is_anagram('abcde','gdbac'))
print(is_anagram('abcde','dbacg'))
print(is_anagram('abcde','edbac'))