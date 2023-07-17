# first make board
import random
board = ["_" , "_" , "_",
         "_" , "_" , "_",
         "_" , "_" , "_"]
game_running =True
winner =None
current_player ="X"

def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("------------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("------------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def inputplayer(board):
    global current_player
    pos= int(input("Enter the position 1-9  "))
    if pos >=1 and pos<=9 and board[pos-1]=="_":
        board[pos-1]=current_player
    else:
        print("oops player has already filled it")

def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="_":
        winner=board[0]
        print("horizontal check")
        return True
    elif board[3]==board[4]==board[5] and board[3]!="_":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="_":
        winner = board[6]
        return True
    return False
def checkvertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="_":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="_":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="_":
        winner = board[2]
        return True
    return False
def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="_":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="_":
        winner = board[3]
        return True
    return False
def switchplayer():
    global current_player
    if current_player =="X":
        current_player="O"
    else:
       # print("in else")
        current_player="X"
 
def checktie(board):
    global game_running
    if "_" not in board:
        printboard(board)
        print("there is a tie")
        game_running=False

def checkwin(board):
    global game_running
    
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        print(f"The winner is {winner}")
        game_running=False
        

def computerplayer(board):
    global current_player
    if current_player =="O":
        position = random.randint(0,8)
        if board[position] =="_":
            board[position]="O"
            switchplayer()

printboard(board)
#print("cur plyer"+current_player)
inputplayer(board)
switchplayer()
printboard(board)
 
while  game_running: 
        #print("cur plyer"+current_player)
   
    computerplayer(board)
    printboard(board)
    checkwin(board)
    checktie(board)
    inputplayer(board)
    checkwin(board)
    checktie(board)
    printboard(board)
    switchplayer()
    


        


    
