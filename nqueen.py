import copy
import random
from collections import deque

class NQueens:
  def __init__(self, size):
    self.size = size

  def conflict(self, queens):
    for i in range(1, len(queens)):
      for j in range(0, i):
        a,b = queens[i]
        c,d = queens[j]
        if a == c or b == d or abs(a-c) == abs(b-d):
          return True
    return False
  
  def get_next_moves(self, queens):
    moves = []
    for i in range(self.size):
      for j in range(self.size):
        new_queens = copy.deepcopy(queens)
        new_queens.append((i,j))
        if not self.conflict(new_queens):
          moves.append(new_queens)
    return moves
  
  def is_goal(self, queens):
    return len(queens) == self.size
  
  def print_board(self, queens):
    board = [['.' for i in range(self.size)] for j in range(self.size)]
    for i in range(self.size):
      a,b = queens[i]
      board[a][b] = 'Q'
    for i in range(self.size):
      print(' '.join(board[i]))
    print() 

  def heuristic(self, queens):
    # returns the number of conflicts 
    return sum([self.conflict(queens[:i]) for i in range(1, len(queens))] + [0])

class BFS:
  def __init__(self, nqueens):
    self.nqueens = nqueens
    self.closed = set()
    self.open = deque()
  
  def search(self):
    self.open.append([])
    while self.open:
      queens = self.open.popleft()
      if self.nqueens.is_goal(queens):
        return queens
      for new_queens in self.nqueens.get_next_moves(queens):
        if tuple(new_queens) not in self.closed:
          self.open.append(new_queens)
          self.closed.add(tuple(new_queens))

class DFS:
  def __init__(self, nqueens):
    self.nqueens = nqueens
    self.closed = set()
    self.open = []
  
  def search(self):
    self.open.append([])
    while self.open:
      queens = self.open.pop()
      if self.nqueens.is_goal(queens):
        return queens
      for new_queens in self.nqueens.get_next_moves(queens):
        if tuple(new_queens) not in self.closed:
          self.open.append(new_queens)
          self.closed.add(tuple(new_queens))

def main():
  size = 4
  nqueens = NQueens(size)
  queens = []
  
  # bfs = BFS(nqueens)
  # queens = bfs.search()

  dfs = DFS(nqueens)
  queens = dfs.search()

  nqueens.print_board(queens)

if __name__ == "__main__":
  main()