import random
def display_board(box):
    #function for displaying TICTAKTOE board
    print(box[1]+"|"+box[2]+"|"+box[3])
    print("-|-|-")
    print(box[4]+"|"+box[5]+"|"+box[6])
    print("-|-|-")
    print(box[7]+"|"+box[8]+"|"+box[9])


#function for both players mark "X" or "O"
def playeInputMark(player):
    player_num = player
    Mchoise = False
    player = ""
    while Mchoise == False:

        player = input(f"{player_num} enter your choise X or O : ").upper()
        if player not in ["X","O"]:
            print("sorry entered value is not valid!")
        else:
            Mchoise = True
    #assigning player1 and player2 mark
    if player_num == "player1" and player in ["X","O"]:
        if player == "X":
            return ["X","O"]
        else:
            return ["O","X"]
    #assigining player2 and player1 mark
    elif player_num == "player2" and player in ["X","O"]:
        if player == "X":
            return ["O","X"]
        else:
            return ["X","O"]

#function for placing mark on the position
def placeMarker(board,mark,position):
    
    board[position] = mark
    print("\n"*10)
    display_board(board)



#weather the player is won or not
def win_check(board,mark):
    return((board[1] == board[2] == board[3] == mark)or
        (board[4] == board[5] == board[6] == mark)or
        (board[7] == board[8] == board[9] == mark)or
        (board[1] == board[4] == board[7] == mark)or
        (board[2] == board[5] == board[8] == mark)or
        (board[3] == board[6] == board[9] == mark)or
        (board[1] == board[5] == board[9] == mark)or
        (board[3] == board[5] == board[7] == mark))

#which player should go first
def choose_first():
    player_no = random.randint(1,2)

    return "player"+str(player_no)
#checking  is there any spaces in board
def space_check(box,position):
    if box[position] != " ":
        return False
    return True

#checking weather the board is full or not
def full_check(box):
    if " " in box:
        return False
    return True

#accepting the users position choise
def player_choise(box):
    Mposition = "Wrong"
    digit = False
    space = False
    while Mposition.isdigit() == False or digit == False or space == False:
    
        Mposition = input("Enter your postion in range(1,9): ")
        #Digit check
        if Mposition.isdigit() == False:
            print("sorry entered value is not a digit")
    
        #Range Check
        if Mposition.isdigit() == True and int(Mposition) not in range(1,10):
            print("Sorry entered digit is not in range (1,9)!")
            digit = False
        #Space Check
        elif Mposition.isdigit() == True and space_check(box,int(Mposition)) == False:
            print("selected position is not empty! choose another ")
        else:
            space = True
            digit = True   
    
    return int(Mposition)

#to countinue the game or not
def replay():
    choise = ""
    while choise not in ["N","Y"]:
        choise = input("to continue 'Y' and to quit 'N': ").upper()
    if choise == 'N':
        return False
    else:
        return True
    
# BUILD GAME LOGIC

game_on = True

while game_on == True:
    print("Welcome To Tic Tak Toe!")
    print('\n'*5 )
    box = ["#"," "," "," "," "," "," "," "," "," "]

    # Displaying board
    display_board(box)                                       

    #ramdomly selects which player should go first
    Cf = choose_first()
    player1,player2 = playeInputMark(Cf)
    #game begines here
    print(f"player1 mark is {player1}\nplayer2 mark is {player2}")
    win = False
    while full_check(box) == False and win == False:
        if Cf == "player1":
            print("player1 enter your position")
            #player1 input choise
            Pchoise = player_choise(box)
            #player1 choise marks on board
            placeMarker(box,player1,Pchoise)
            #checks weather the player1 won or not
            win = win_check(box,player1)
            if win == True:
                print("HURRY PLAYER 1 WON THE GAME")
                win = True
                
            Cf = "player2"
        else:
            print("player2 enter your position")
            #player2 input choise
            Pchoise = player_choise(box)
            #player2 choise marks on board
            placeMarker(box,player2,Pchoise)
            #checks weather the player2 won or not
            win = win_check(box,player2)
            if win == True:
                print("HURRYYY PLAYER 2 WON THE GAME")
                win = True
            Cf = "player1"
    #if game was tie
    if win == False:
        print("GAME IS ON TIE!")
        
    #weather to continue the game or not    
    game_on = replay()
