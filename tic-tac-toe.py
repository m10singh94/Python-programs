numpad = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def board():
    for i in range(1,10):
        print(f'   {numpad[str(i)]}   ', end="")
        if(i%3 != 0):
            print('|', end="")
        elif (i!=9):
            print('\n-----------------------')

def modify_board(num,ch):
    numpad[str(num)] = ch
    print('\n')
    board()
    print('\n')

def invalid_entry(num):
    if(num > 9 or num < 1):
        return 1
    else:
        return 0

def checkForWin():
    if((numpad['1'] == numpad['2'] and numpad['2'] == numpad['3']) or (numpad['4'] == numpad['5'] and numpad['5'] == numpad['6']) or (numpad['7'] == numpad['8'] and numpad['8'] == numpad['9']) or
    (numpad['1'] == numpad['4'] and numpad['4'] == numpad['7']) or (numpad['2'] == numpad['5'] and numpad['5'] == numpad['8']) or (numpad['3'] == numpad['6'] and numpad['6'] == A['9']) or
    (numpad['1'] == numpad['5'] and numpad['5'] == numpad['9']) or (numpad['3'] == numpad['5'] and numpad['5'] == numpad['7'])):
        return 1
    else:
        return 0

print("Welcome to Tic-Tac-Toe Game")
board()
print("")
leave = 'Y'
count = 1
while(leave != 'N' or leave != 'n'):
    if(count%2 == 0):
        print('Player 2: ', end="")
        ch = 'O'
    else:
        print('Player 1: ', end="")
        ch = 'X'
    num = int(input('Enter the place index(0-9) : '))
    while(invalid_entry(num)):
        print('Invalid Entry. Enter valid index (0-9)')
        num = int(input('Enter the place index(0-9) : '))
    # print(num)
    modify_board(num,ch)
    if(count == 9):
        print('Match tied.')
        break
    count += 1
    if(checkForWin()):
        print('Congratulations!!! You Win.') 
        


