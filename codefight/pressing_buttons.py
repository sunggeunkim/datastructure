'''
reference - https://codefights.com/interview-practice/task/SyBbdPYC86RdkKvjH
Given a string of digits, return all of the possible non-empty letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:



The resulting array should be sorted lexicographically.

Example

For buttons = "42", the output should be
pressingButtons(buttons) = ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"].

Input/Output

[time limit] 4000ms (py3)
[input] string buttons

A string composed of digits ranging from '2' to '9'.

Guaranteed constraints:

0 ≤ buttons.length ≤ 7.

[output] array.string
'''
def pressingButtons(buttons):
    mapping = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ''
    }
    if not buttons:
        return []

    # Use list indexing to get keys and map into answers
    out = [x for x in mapping[buttons[0]]]
    for i in range(1, len(buttons)):
        out = [x + y for x in out for y in mapping[buttons[i]]]

    return out


def pressingButtons_new(buttons):
    if buttons == "":
        return []
    bn = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
          "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"], "*": [],
          "0": [], "#": []}
    output = []
    stack = []
    n = len(buttons)
    i = 0
    while i < n and bn[buttons[i]] == []:
        i += 1

    if i == n:
        return output
    for c in bn[buttons[i]]:
        stack.append((i, c))
    while len(stack) > 0:
        i, c = stack.pop()
        if i < n - 1:
            for newc in bn[buttons[i + 1]]:
                stack.append((i + 1, c + newc))
        else:
            output.insert(0, c)
    return output


print(pressingButtons("42"))
print(pressingButtons_new("42"))


