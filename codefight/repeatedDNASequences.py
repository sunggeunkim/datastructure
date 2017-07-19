'''
reference - https://codefights.com/interview-practice/task/jMwWcx8spsByhiyeJ

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T.
In research, it can be useful to identify repeated sequences within DNA.

Write a function to find all the 10-letter sequences (substrings) that occur more than once in a DNA molecule s,
and return them in lexicographical order. These sequences can overlap.

Example

For s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", the output should be
repeatedDNASequences(s) = ["AAAAACCCCC", "CCCCCAAAAA"].

Input/Output

[time limit] 4000ms (py3)
[input] string s

Guaranteed constraints:
0 ≤ s.length ≤ 5000.

[output] array.string

An array containing all of the potential 10-letter sequences that occur more than once in s.

'''
def repeatedDNASequences(s):
    sset = set()
    result = set()
    for i in range(len(s) - 9):
        s10 = s[i:i+10]
        if s10 in sset:
            result.add(s10)
        else:
            sset.add(s10)
    return sorted(list(result))
