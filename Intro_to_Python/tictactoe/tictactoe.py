import random

def reset():
    board = ['0', '1', '2',
        '3', '4', '5',
        '6', '7', '8']
    return board
end = False
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def show():
    print(board[0], '|',board[1],'|',board[2])
    print('----------')
    print(board[3],'|',board[4],'|',board[5])
    print('----------')
    print(board[6],'|',board[7],'|',board[8])
board = reset()
i  = True
p1 = False
count = 0
while i:
    p1 = not p1
    b = int(input("Pick a space: "))
    if board[b] != 'x' and  board[b] != 'o':
        b = int(b)
        if b <= 8 and b > -1 and board[b] != 'x' and board[b] != 'o' and p1:
            board[b] = 'x'
        b = int(b)
        if b <= 8 and board[b] != 'o' and board[b] != 'x':
            board[b] = 'o'
        show()
        for b in win:
            if board[b[0]] == 'x' and board[b[1]] == 'x' and board[b[2]] == 'x':
                w = input("Player One won the game! Play again?(Y/N?)")
                if w == 'Y':
                    board = reset()
                elif w == 'N':
                    i = False
                    break
        for b in win: 
            if board[b[0]] == 'o' and board[b[1]] == 'o' and board[b[2]] == 'o':
                w = input("Player Two won the game! Play again?(Y/N?)")
                if w == 'Y':
                    board = reset()
                elif w == 'N':
                    i = False
                    break
        count = 0
        for b in range(9):
            if board[b] == 'x' or board[b] == 'o':
                count += 1
            if count ==  9:
                w = input("It's a tie. Play Again?(Y/N)?")
                if w == 'Y':
                    board = reset()
                    count = 0
                elif w == 'N':
                    i = False
                    break

    else:
        print('I\'m sorry, Dave. I\'m afraid I can\'t do that.')

