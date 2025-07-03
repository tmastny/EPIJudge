from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    def dfs(row, col):
        if (
            row < 0 or row == len(board) or
            col < 0 or col == len(board[0]) or
            board[row][col] != "W"
        ):
            return
        
        board[row][col] = "F"
        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            dfs(x, y)
        
    for r in [0, len(board) - 1]:
        for c in range(len(board[0])):
            dfs(r, c)
    
    for c in [0, len(board[0]) - 1]:
        for r in range(len(board)):
            dfs(r, c)
  
    # set interior whites to black
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "W":
                board[r][c] = "B"
    
    # reset free boundary Ws to W
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "F":
                board[r][c] = "W"
    
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
