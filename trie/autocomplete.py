'''
Write an autocomplete class that returns all dictionary words with a given prefix

e.g.
dict:   {"abc", "acd", "bcd", "def", "a", "aba"}
 
prefix: "a" -> "abc", "acd", "a", "aba"
prefix: "b" -> "bcd"

reference: http://www.byte-by-byte.com/autocomplete/
'''

# Trie node class
class Node:
    def __init__(self, prefix):
        self.prefix = prefix
        self.children = dict()
        self.isWord = None


class Autocomplete:

    # construct the trie from the dictionary (list of words)
    def __init__(self, d):
        self.trie = Node("")
        for s in d:
            self.insertWord(s)

    # insert a word (string) into the trie
    def insertWord(self, s):
        curr = self.trie

        # iterate through each character in the string
        for i in range(len(s)):

            # if the character is not in the children then add a node
            if s[i] not in curr.children:
                curr.children[s[i]] = Node(s[i])
            curr = curr.children[s[i]]

            # for the last character, set the isWord flag
            if i == len(s) - 1: curr.isWord = True

    # find all words in trie that start with prefix
    def getWordForPrefix(self,pre):
        results = []

        curr = self.trie
        for c in pre:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return results

        # at the end of the prefix, find all child words
        self.findAllChildWords(curr, results, pre)
        return results

    # recursively find all child words
    def findAllChildWords(self, curr, results, prefix):
        if curr.isWord:
            results.append(prefix)
        for c in curr.children:
            self.findAllChildWords(curr.children[c], results, prefix + c)

ac = Autocomplete(["abc", "acd", "bcd", "def", "a", "aba"])

print(ac.getWordForPrefix("a"))
print(ac.getWordForPrefix("ab"))
print(ac.getWordForPrefix("b"))
print(ac.getWordForPrefix("d"))
