'''
ref: https://codefights.com/interview-practice/task/awcwfd2TXRvoFhnPH

In chess, queens can move any number of squares vertically, horizontally, or diagonally. You have an n × n chessboard with some queens on it. You are given several queries, each of which represents one square on the chessboard. For each query square, determine whether it can be attacked by a queen or not.

Example

For n = 5, queens = [[1, 1], [3, 2]] and queries = [[1, 1], [0, 3], [0, 4], [3, 4], [2, 0], [4, 3], [4, 0]], the output should be
squaresUnderQueenAttack(n, queens, queries) = [true, false, false, true, true, true, false].
'''

def squaresUnderQueenAttack(n, queens, queries):
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()
    res = []
    for queen in queens:
        rows.add(queen[0])
        cols.add(queen[1])
        diag1.add(queen[0] + queen[1])
        diag2.add(queen[1] - queen[0])
    for query in queries:
        if query[0] in rows or query[1] in cols or query[0] + query[1] in diag1 or query[1] - query[0] in diag2:
            res.append(True)
        else:
            res.append(False)
    return res

