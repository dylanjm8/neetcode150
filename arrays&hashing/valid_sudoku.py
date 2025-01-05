class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no assumptions are made for empty spots in this problem, makes it easier, ie an empty spot that must be a 9 but cant due to rules
        # so only looking for duplicates
        # using a hashset to represent the different 3x3 grids
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key of c/3 r/3

        for r in range (9):
            for c in range(9):
                if board[r][c] == ".":
                    continue # skipping empty "." elements shown in the sudoku board
                if (board[r][c] in rows[r] or # CURRENT row -> hence [r]
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3]): # // 3 mean divided by three and rounded down nearest int (low floor division)
                    return False
                cols[c].add(board[r][c]) # want to update all hashmaps (sets)
                rows[r].add(board[r][c])
                squares[(r // 3),(c // 3)].add(board[r][c])

        return True
                    
# In this case a technical hasmap is used though it is practically a hashset since there is no use of key value pairs, 
# instead the key is technically the column or row numbers (or r//3 c//3) instead with no pairs (pairs are filled later!) which allows for iteration through the set through keys




