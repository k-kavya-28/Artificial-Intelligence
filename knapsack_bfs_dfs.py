import copy
from queue import deque
class knapsack:

    def __init__(self,capacity):
        self.profit=0
        self.weight=0
        self.capacity = capacity
        self.itemselected=0

    def additem(self,p,w):
            new_knapsack=copy.deepcopy(self)
            new_knapsack.profit+=p
            new_knapsack.weight+=w
            new_knapsack.itemselected+=1
            return new_knapsack
    
    def dontadditem(self):
         new_knapsack=copy.deepcopy(self)
         new_knapsack.itemselected=new_knapsack.itemselected+1
         return new_knapsack

def bfs(k):
    open_list=deque([k])
    closed_list=set()

    max_profit=0

    while open_list:
          selected_element=open_list.popleft()
          closed_list.add(tuple((selected_element.profit,selected_element.weight)))
          current_profit=selected_element.profit

          if current_profit>max_profit:
               #update
               max_profit=current_profit
          if selected_element.itemselected<len(pr):
             possible_moves=[selected_element.additem(pr[selected_element.itemselected],we[selected_element.itemselected]),selected_element.dontadditem()]
          
             for move in possible_moves:
                  if move.weight<=move.capacity:
                      open_list.append(move)
    
    return max_profit 


def dfs(k):
     open_list=[k]
     closed_list=set()

     max_profit=0

     while open_list:
          selected_element=open_list.pop(-1)
          closed_list.add(tuple((selected_element.profit,selected_element.weight)))

          current_profit=selected_element.profit
          
          #update
          if current_profit>max_profit:
               max_profit=current_profit
               #print("max profit:",max_profit)
          if selected_element.itemselected<len(pr):
               
               possible_moves=[selected_element.additem(pr[selected_element.itemselected],we[selected_element.itemselected]),selected_element.dontadditem()]

               for move in possible_moves:
                    if move.weight<=move.capacity:
                         open_list.append(move)
     return max_profit


pr = [20, 30, 40, 100]
we = [70, 80, 90, 200]
k=knapsack(100)
bfsprofit=bfs(k)
print("bfs profit:",bfsprofit)
dfsprofit=dfs(k)
print("dfsprofit",dfsprofit)






