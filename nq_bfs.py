from collections import deque

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

def nq_bfs(N):
    solutions = []
    queue = deque([([],0)]) #board, row
    
    while queue:
        board, row = queue.popleft()
        if row == N:
            solutions.append(board)
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    new_board = [row.copy() for row in board]
                    new_board.append([1 if j == col else 0 for j in range(N)])
                    queue.append((new_board, row + 1))
    return solutions

def print_solution(solution):
    for row in solution:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    print()
    
N=5
solutions = nq_bfs(N)
for solution in solutions:
    print_solution(solution)