def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,N)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, row, N, solutions):
    if row == N:
        solutions.append([row[:] for row in board])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col]=1
            solve_nq_util(board, row+1, N, solutions)
            board[row][col]=0
        

def solve_nq(N):
    board = [[0]*N for _ in range(N)]
    solutions = []
    solve_nq_util(board, 0, N, solutions)
    return solutions

def print_solution(solution):
    for row in solution:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    print()
    
N=5
solutions = solve_nq(N)
for solution in solutions:
    print_solution(solution)