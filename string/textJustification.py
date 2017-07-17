'''
reference: https://codefights.com/interview-practice/task/rak3HBvHDAjHRkTCW/description
Given an array of words and a length l, format the text such that each line has exactly l characters and is fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack as many words as possible in each line. Add extra spaces when necessary so that each line has exactly l characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text and lines with one word only, the words should be left justified with no extra space inserted between them.

Example

For
words = ["This", "is", "an", "example", "of", "text", "justification."]
and l = 16, the output should be

textJustification(words, l) = ["This    is    an",
                               "example  of text",
                               "justification.  "]
Input/Output

[time limit] 4000ms (py3)
[input] array.string words

An array of words. Each word is guaranteed not to exceed l in length.

Guaranteed constraints:
1 ≤ words.length ≤ 150,
0 ≤ words[i].length ≤ l.

[input] integer l

The length that all the lines in the output array should be.

Guaranteed constraints:
1 ≤ l ≤ 60.

[output] array.string

The formatted text as an array containing lines of text, with each line having a length of l.
'''

def just(words, L):
    if len(words) == 1:
        return words[0] + (L - len(words[0])) * " "
    spaces = L - sum(map(len, words))
    minspace = (spaces // (len(words) - 1)) * " "
    extraspace = spaces % (len(words) - 1)
    line = ""
    for i, word in enumerate(words[:-1]):
        line += word + minspace + (" " if i < extraspace else "")
    line += words[-1]
    return line

def textJustification(words, L):
    lines = []
    line = []
    l = -1
    for word in words:
        if l + 1 + len(word) > L:
            lines.append(just(line, L))
            l = -1
            line = []
        line.append(word)
        l += 1 + len(word)
    line = " ".join(line)
    line += (L - len(line)) * " "
    lines.append(line)
    return lines
        

