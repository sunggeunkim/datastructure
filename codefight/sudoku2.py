#find if the input grid is a valid sudoku game
#grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# sudoku2(grid) = True
# [input] array.array.char grid
# A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.
#
# [output] boolean
# Return true if grid represents a valid Sudoku puzzle, otherwise return false.

def sudoku2(grid):    
    for r in range(9):
        a = [0] * 9
        for c in range(9):
            if grid[r][c] == '.':
                continue
            if a[int(grid[r][c])-1] == 1:
                return False
            a[int(grid[r][c])-1] = 1
    for c in range(9):
        a = [0] * 9
        for r in range(9):
            if grid[r][c] == '.':
                continue
            if a[int(grid[r][c])-1] == 1:
                return False
            a[int(grid[r][c])-1] = 1
    for r in range(0,9,3):
        for c in range(0,9,3):
            a = [0] * 9
            for i in range(3):
                for j in range(3):
                    if grid[r+i][c+j] == '.':
                        continue
                    if a[int(grid[r+i][c+j])-1] == 1:
                        return False
                    a[int(grid[r+i][c+j])-1] = 1
    return True
