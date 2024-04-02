from collections import deque

class Hanoi:
  def _init_(self, n):
    self.n = n
    self.towers = [[], [], []]
    self.towers[0] = list(range(n, 0, -1))

  def move_disk(self, src, dest):
    if not self.towers[src]: # no disc
      return False
    if self.towers[dest] and self.towers[dest][-1] < self.towers[src][-1]: # smaller disc
      return False
    self.towers[dest].append(self.towers[src].pop()) # move disc
    return True
  
  def get_next_moves(self):
    moves = []
    for src in range(3):
      for dest in range(3):
        if src != dest and self.move_disk(src, dest):
          moves.append((src, dest))
          self.move_disk(dest, src)
    return moves

  def is_goal(self):
    return not self.towers[0] and not self.towers[1] 
  
class BFS:
  def _init_(self, hanoi) -> None:
    self.hanoi = hanoi
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append((self.hanoi, []))
    while self.open:
      hanoi, path = self.open.popleft()
      if hanoi.is_goal():
        return path
      elif hanoi.towers not in self.closed:
        self.closed.append(hanoi.towers)
        for move in hanoi.get_next_moves():
          new_hanoi = Hanoi(hanoi.n)
          new_hanoi.towers = [list(tower) for tower in hanoi.towers]
          new_hanoi.move_disk(move[0], move[1])
          self.open.append((new_hanoi, path+[move]))
    return None
  
def main():
  hanoi = Hanoi(3)
  bfs = BFS(hanoi)
  path = bfs.search()
  print(path)

if __name__ == '_main_':
  main()