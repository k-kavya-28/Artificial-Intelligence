# Assignment 1, Task 1
# Write a Program for Tic-Tac-Toe game between two human players. The functions for printing
#Tic-Tac-Toe board, IsWinner() and playerMove() are already given for your help.board = [' ' for x in range(10)]

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
        move = input("Please select a position to enter the {sym} between 1 to 9: ".format(sym=symbol))
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
    
def main():
    print('Welcome to Tic-Tac-Toe!')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(IsWinner(board, 'O')):
            playerMove('X')
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break
        if not(IsWinner(board, 'X')):
            playerMove('O')
            printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break
    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play ? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

if __name__ == '__main__':
    main()