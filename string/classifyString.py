'''
reference: https://codefights.com/interview-practice/task/Ss4qyHoGJQhpvaGWc
You categorize strings into three types: good, bad, or mixed. If a string has 3 consecutive vowels or 5 consecutive consonants, or both, then it is categorized as bad. Otherwise it is categorized as good. Vowels in the English alphabet are ["a", "e", "i", "o", "u"] and all other letters are consonants.

The string can also contain the character ?, which can be replaced by either a vowel or a consonant. This means that the string "?aa" can be bad if ? is a vowel or good if it is a consonant. This kind of string is categorized as mixed.

Implement a function that takes a string s and returns its category: good, bad, or mixed.

Example

For s = "aeu", the output should be
classifyStrings(s) = "bad";

For s = "a?u", the output should be
classifyStrings(s) = "mixed";

For s = "aba", the output should be
classifyStrings(s) = "good".

Input/Output

[time limit] 4000ms (py3)
[input] string s

A string that can contain only lowercase English letters and the character ?.

Guaranteed constraints:
1 ≤ s.length ≤ 50.

[output] string

good, bad or mixed.
'''


def classifyStrings(s):
    vowels_list = "aeiou"
    vowels, consonants, mixedVowels, mixedConsonants = 0, 0, 0, 0
    bad = False
    mixed = False
    for i in range(len(s)):
        char = s[i]
        if char == "?":
            vowels, consonants = 0, 0
            mixedVowels += 1
            mixedConsonants += 1
            if mixedVowels > 2:
                consonants += 1
            elif mixedConsonants > 4:
                vowels += 1
            if i > 0 and s[i - 1] == '?':
                vowels, consonants = 0, 0
        elif char in vowels_list:
            vowels += 1
            mixedVowels += 1
            consonants, mixedConsonants = 0, 0
        else:
            consonants += 1
            mixedConsonants += 1
            vowels, mixedVowels = 0, 0
        bad = bad or (vowels > 2 or consonants > 4)
        mixed = mixed or (mixedVowels > 2 or mixedConsonants > 4)
    return "bad" if bad else "mixed" if mixed else "good"

