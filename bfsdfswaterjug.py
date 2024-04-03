import copy
from collections import deque

class Jug:
  def __init__(self, cap) -> None:
    self.cap = cap
    self.curr = 0

  def fill(self, amt):
    if self.curr+amt<=self.cap:
      self.curr += amt
      return True
    return False

  def empty(self):
    self.curr = 0

  def transfer(self, jug):
    if self.fill(jug.curr):
      jug.empty()
      return True
    return False

  def printState(self):
    print(f"Curr: {self.curr}, Cap: {self.cap}")

def getNextMove(jug1, jug2):
  moves = []

  if jug1.curr < jug1.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug1.fill(jug1.cap - jug1.curr)
    moves.append((new_jug1, jug2))

  if jug2.curr < jug2.cap:
    new_jug2 = copy.deepcopy(jug2)
    new_jug2.fill(jug2.cap - jug2.curr)
    moves.append((jug1, new_jug2))

  if jug1.curr > 0:
    new_jug1 = copy.deepcopy(jug1)
    new_jug1.empty()
    moves.append((new_jug1, jug2))

  if jug2.curr > 0:
    new_jug2 = copy.deepcopy(jug2)
    new_jug2.empty()
    moves.append((jug1, new_jug2))

  # Pour from jug1 to jug2
  if jug1.curr > 0 and jug2.curr < jug2.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug2 = copy.deepcopy(jug2)
    while new_jug1.curr > 0 and new_jug2.curr < new_jug2.cap:
      new_jug2.fill(1)
      new_jug1.empty()
      moves.append((new_jug1, new_jug2))

  # Pour from jug2 to jug1
  if jug2.curr > 0 and jug1.curr < jug1.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug2 = copy.deepcopy(jug2)
    while new_jug2.curr > 0 and new_jug1.curr < new_jug1.cap:
      new_jug1.fill(1)
      new_jug2.empty()
      moves.append((new_jug1, new_jug2))

  return moves

class BFS:
  def __init__(self, jug1, jug2):
    self.jug1 = jug1
    self.jug2 = jug2
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append((self.jug1, self.jug2, []))
    while self.open:
      jug1, jug2, path = self.open.popleft()
      if jug1.curr==2:
        return path
      elif (jug1.curr, jug2.curr) not in self.closed:
        self.closed.append((jug1.curr, jug2.curr))
        for move in getNextMove(jug1, jug2):
          self.open.append((move[0], move[1], path+[move]))
    return None

class DFS:
  def __init__(self, jug1, jug2) -> None:
    self.jug1 = jug1
    self.jug2 = jug2
    self.closed = []
    self.open = []

  def search(self):
    self.open.append((self.jug1, self.jug2, []))
    while self.open:
      jug1, jug2, path = self.open.pop()
      if jug1.curr==2:
        return path
      elif (jug1.curr, jug2.curr) not in self.closed:
        self.closed.append((jug1.curr, jug2.curr))
        for move in getNextMove(jug1, jug2):
          self.open.append((move[0], move[1], path+[move]))
    return None

def main():
  jug1 = Jug(4)
  jug2 = Jug(3)
  # bfs = BFS(jug1, jug2)
  # path = bfs.search()
  dfs = DFS(jug1, jug2)
  path = dfs.search()
  if path is None:
    print('No solution found')
  else:
    for state in path:
      state[0].printState()
      state[1].printState()
      print()

if __name__ == '__main__':
  main()