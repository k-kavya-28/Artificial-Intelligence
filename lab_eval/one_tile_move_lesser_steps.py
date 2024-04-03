import copy
import heapq

class PuzzleNode:
    def init(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = self.calHeuristic()

    def lt(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic
  
    def calHeuristic(self):
        dis = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j]!=0:
                dis += abs(i-(self.state[i][j]-1)//3)+abs(j-(self.state[i][j]-1)%3)
        return dis
  
  def isGoal(self):
    return self.state == goal 
  
  def getBlanks(self):
    blanks = []
    for i in range(3):
      for j in range(3):
        if self.state[i][j]==0:
          blanks.append((i,j))
    return blanks
  
  def getSuccessors(self):
    moves = []
    blanks = self.getBlanks()
    for blank in blanks:
      for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
        newx = blank[0]+dir[0]
        newy = blank[1]+dir[1]
        if 0<=newx<3 and 0<=newy<3:
          new_state = copy.deepcopy(self.state)
          new_state[blank[0]][blank[1]] = new_state[newx][newy]
          new_state[newx][newy] = 0
          moves.append(PuzzleNode(new_state, parent=self, cost=self.cost+1))
    return moves
  
  def getPath(self):
    path = []
    current = self
    while current is not None:
      path.append(current.state)
      current = current.parent
    return path[::-1]
  
def search(initial):
  vis = set()
  pq = []
  heapq.heappush(pq, initial)
  while pq:
    curr = heapq.heappop(pq)
    if curr.isGoal():
      return curr.getPath()
    vis.add(tuple(map(tuple, curr.state)))

    for succ in curr.getSuccessors():
      if tuple(map(tuple, succ.state)) not in vis:
        heapq.heappush(pq, succ)
  return None


initial = [[0, 3, 6], [1, 2, 0], [4, 5, 7]]
goal = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

initial_node = PuzzleNode(initial)
result = search(initial_node)
if result:
  for state in result:
    for row in state:
      print(row)
    print()
else:
  print("No solution found")