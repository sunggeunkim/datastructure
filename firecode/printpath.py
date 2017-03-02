def connect(board, i, j, path):
    nrow = len(board)
    ncol = len(board[0])
    if i<nrow and j<ncol:
        path += board[i][j]
    if i==nrow-1 and j==ncol-1:
        return [path]
    path_list = []
    if i < nrow:
        path0 = str(path)
        new_path0 = connect(board, i+1, j, path0)
        path_list += new_path0
    if j < ncol:
        path1 = str(path)
        new_path1 = connect(board, i, j+1, path1)
        path_list += new_path1
    return path_list
    
def print_paths(board):
    path = ''
    return connect(board,0,0,path)

board=[
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L'],
  ['M', 'N', 'O', 'P']
]

print(print_paths(board))
