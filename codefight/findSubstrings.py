'''
ref:https://codefights.com/interview-practice/task/Ki9zRh5bfRhH6oBau

You have two arrays of strings, words and parts. 
Return an array that contains the strings from words, 
modified so that any occurrences of the substrings from parts are surrounded by square brackets [], 
following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. 
If there is still more than one such part, then choose the one that appears first in the string.

Example

For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
findSubstrings(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, 
"a", "mel", and "lon", "mel" is the longest substring that appears first in the string.

Input/Output

[time limit] 4000ms (py3)
[input] array.string words

An array of strings consisting only of uppercase and lowercase English letters.

Guaranteed constraints:
0 ≤ words.length ≤ 104,
1 ≤ words[i].length ≤ 30.

[input] array.string parts

An array of strings consisting only of uppercase and lower English letters. Each string is no more than 5 characters in length.

Guaranteed constraints:
0 ≤ parts.length ≤ 105,
1 ≤ parts[i].length ≤ 5,
parts[i] ≠ parts[j].

[output] array.string
'''


def findSubstrings(words, parts):
    parts = set(parts)
    results = list(words)
    for i, word in enumerate(words):
        longest = 0
        for k in range(len(word)):
            for l in range(5, 0, -1):
                if word[k:k+l] in parts and len(word[k:k+l]) > longest:
                    longest = len(word[k:k+l])
                    results[i] = word[:k] + "[" + word[k:k+l] + "]" + word[k+l:]
    return results
