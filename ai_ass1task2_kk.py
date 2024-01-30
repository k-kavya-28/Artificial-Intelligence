# Assignment 1
# Task 2 : Replace one Human player with rule based AI Program. 
# Simple Reflex Agent 

board = [' ' for x in range(10)]

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def IsWinner(b, l):
    return (b[1] == l and b[2] == l and b[3] == l) or \
           (b[4] == l and b[5] == l and b[6] == l) or \
           (b[7] == l and b[8] == l and b[9] == l) or \
           (b[1] == l and b[4] == l and b[7] == l) or \
           (b[3] == l and b[6] == l and b[9] == l) or \
           (b[2] == l and b[5] == l and b[8] == l) or \
           (b[1] == l and b[5] == l and b[9] == l) or \
           (b[3] == l and b[5] == l and b[7] == l)

def spaceIsFree(pos):
    return board[pos] == ' '

def insertLetter(letter, pos):
    board[pos] = letter

def playerMove(symbol):
    run = True
    while run:
        move = input(f"Please select a position to enter the {symbol} between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter(symbol, move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number between 1 and 9')
        except:
            print('Please type a number')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def selectRandom(li):
  import random
  ln = len(li)
  r = random.randrange(0, ln)
  return li[r]

def canPlayerWin(board, symbol):
  for i in range(1, 10):
    if spaceIsFree(i):
      boardCopy = board[:]
      boardCopy[i] = symbol
      if IsWinner(boardCopy, symbol):
        return i
  return -1

def getComputerMove():
  move = canPlayerWin(board, 'O')
  if move != -1:
    return move
  else:
    move = canPlayerWin(board, 'X')
    if move != -1:
      return move
    else:
      if spaceIsFree(5):
        return 5
      else:
        move = selectRandom([1, 3, 7, 9])
        if spaceIsFree(move):
          return move
        else:
          return selectRandom([2, 4, 6, 8])
        
def getComputerMove2():
  if(board[1]=='X' and board[2]=='X' and board[3]==' '):
    return 3
  elif(board[1]=='X' and board[2]==' ' and board[3]=='X'):
    return 2
  elif(board[1]==' ' and board[2]=='X' and board[3]=='X'):
    return 1
  
  elif(board[4]=='X' and board[5]=='X' and board[6]==' '):
    return 6
  elif(board[4]=='X' and board[5]==' ' and board[6]=='X'):
    return 5
  elif(board[4]==' ' and board[5]=='X' and board[6]=='X'):
    return 4
  
  elif(board[7]=='X' and board[8]=='X' and board[9]==' '):
    return 9
  elif(board[7]=='X' and board[8]==' ' and board[9]=='X'):
    return 8
  elif(board[7]==' ' and board[8]=='X' and board[9]=='X'):
    return 7
  
  elif(board[1]=='X' and board[4]=='X' and board[7]==' '):
    return 7
  elif(board[1]=='X' and board[4]==' ' and board[7]=='X'):
    return 4
  elif(board[1]==' ' and board[4]=='X' and board[7]=='X'):
    return 1
  
  elif(board[2]=='X' and board[5]=='X' and board[8]==' '):
    return 8
  elif(board[2]=='X' and board[5]==' ' and board[8]=='X'):
    return 5
  elif(board[2]==' ' and board[5]=='X' and board[8]=='X'):
    return 2
  
  elif(board[3]=='X' and board[6]=='X' and board[9]==' '):
    return 9  
  elif(board[3]=='X' and board[6]==' ' and board[9]=='X'):
    return 6
  elif(board[3]==' ' and board[6]=='X' and board[9]=='X'):
    return 3
  
  elif(board[1]=='X' and board[5]=='X' and board[9]==' '):
    return 9
  elif(board[1]=='X' and board[5]==' ' and board[9]=='X'):
    return 5
  elif(board[1]==' ' and board[5]=='X' and board[9]=='X'):
    return 1
  
  elif(board[3]=='X' and board[5]=='X' and board[7]==' '):
    return 7
  elif(board[3]=='X' and board[5]==' ' and board[7]=='X'):
    return 5
  elif(board[3]==' ' and board[5]=='X' and board[7]=='X'):
    return 3
  
  else:
    return -1
  
def getRandomMove(board):
  possibleMoves = []
  for i in range(1, 10):
    if spaceIsFree(i):
      possibleMoves.append(i)
  move = selectRandom(possibleMoves)
  return move

def main():
  printBoard(board)
  for _ in range(5):
    playerMove('X')
    printBoard(board)
    if IsWinner(board, 'X'):
      print('X won!')
      break
    if isBoardFull(board):
      print('Tie game!')
      break
    move = getComputerMove2()
    if move == -1:
      insertLetter('0', getRandomMove(board))
      print('Computer placed an \'O\' in position', move, ':')
      printBoard(board)
    else:
      insertLetter('O', move)
      print('Computer placed an \'O\' in position', move, ':')
      printBoard(board)
    if IsWinner(board, 'O'):
      print('O won!')
      break



if __name__ == "__main__":
    main()
