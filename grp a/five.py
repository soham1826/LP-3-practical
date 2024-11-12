# Python3 program to solve N Queen Problem using backtracking
global N 
N = 4

def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end=" ") 
        print() 

# A utility function to check if a queen can be placed on board[row][col]. 
# We only check left side for attacking queens since queens are placed column by column.
def isSafe(board, row, col): 
    # Check this row on the left side
    for i in range(col): 
        if board[row][i] == 1: 
            return False 

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 

    return True 

def solveNQUtil(board, col): 
    # Base case: If all queens are placed, return true
    if col >= N: 
        return True 

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N): 
        if isSafe(board, i, col): 
            # Place this queen in board[i][col]
            board[i][col] = 1 

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1) == True: 
                return True 

            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove the queen (backtrack)
            board[i][col] = 0 

    # If the queen cannot be placed in any row in this column, return false
    return False 

# This function solves the N Queen problem using Backtracking.
# It returns false if no solution exists, otherwise it prints the solution.
def solveNQ(): 
    board = [[0, 0, 0, 0], 
             [0, 0, 0, 0], 
             [0, 0, 0, 0], 
             [0, 0, 0, 0]] 

    if solveNQUtil(board, 0) == False: 
        print("Solution does not exist") 
        return False 

    printSolution(board) 
    return True 

# Run the solver
solveNQ()

