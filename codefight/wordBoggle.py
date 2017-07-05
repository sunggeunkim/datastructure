'''
ref: https://codefights.com/interview-practice/task/v3uf4PGocp2CH62nn

Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.

Example

For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
wordBoggle(board, words) = ["CODE", "RULES"].
'''

def searchboard(board, c):
    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == c:
                result.append((i, j))
    return result

def wordBoggle(board, words):
    if len(words) == 0: return words
    nrow = len(board)
    ncol = len(board[0])
    result = set()
    for word in words:
        first_found = searchboard(board, word[0])
        if len(first_found) == 0: continue
        s = []
        for first in first_found:
            s.append((first[0], first[1], 0, set()))
        while len(s):
            i, j, l, visited = s.pop()
            visited.add((i,j))
            if l == len(word)-1:
                result.add(word)
            else:
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        if ni == i and nj == j:
                            continue
                        if 0<=ni<=nrow-1 and 0<=nj<=ncol-1\
                                and (ni, nj) not in visited\
                                and board[ni][nj] == word[l+1]:
                            s.append((ni, nj, l+1, set(visited)))
    return sorted(list(result))

