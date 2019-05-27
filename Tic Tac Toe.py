#Blog address: notforcedtodothis.wordpress.com
import random
import pickle
def menu_start():#menu for game
    """
    Display the initial menu.
    
    This will display a menu asking the number of players, and return
    this to the main program. Also present the option to load an already saved game.

    :returns:  The number of players in the game
    """
    type_game=int(input('1)1 player game \n'
                        '2)2 player game \n'
                        '3)Load a saved game \n'
                         'Type the corressponding number '))
    if type_game==1:#For a one player game
        print("You chose a one player game. Don't you have any friends to play with?")
        board()
        play()
    elif type_game==2:   #For a two player game     
        print('You chose a two player game. I see you finally made friends.')
        board()
        two_player()
    elif type_game==3:#To load an already saved game
        load()
        board()
        play()
    else: #Otherwise return error value
        print('Please enter a valid number')
        menu_start()
    
game_board=[0,1,2,3,4,5,6,7,8]

 
def board():#Sets the game board
    '''
    Displays the game board

    Prints the game board at the beginning of the game before any move.
    '''
    print (game_board[0], '|', game_board[1], '|', game_board[2])
    print ('---------')
    print (game_board[3], '|', game_board[4], '|', game_board[5])
    print ('---------')
    print (game_board[6],'|', game_board[7],'|', game_board[8])
    


def checkwin(): #Checks whether there is a winner 
    '''
    Checks if any player has won.

    Function that detects any winners within the game according to all the possible outcomes

    :returns: the winner if condition is satisfied.
    '''
    if    (game_board[0]=='x' and game_board[1]=='x' and game_board[2]=='x')\
       or (game_board[0]=='x' and game_board[4]=='x' and game_board[8]=='x')\
       or (game_board[0]=='x' and game_board[3]=='x' and game_board[6]=='x')\
       or (game_board[2]=='x' and game_board[5]=='x' and game_board[8]=='x')\
       or (game_board[3]=='x' and game_board[4]=='x' and game_board[5]=='x')\
       or (game_board[6]=='x' and game_board[7]=='x' and game_board[8]=='x')\
       or (game_board[6]=='x' and game_board[4]=='x' and game_board[2]=='x')\
       or (game_board[1]=='x' and game_board[4]=='x' and game_board[7]=='x'):
        return 'x'
    elif    (game_board[0]=='o' and game_board[1]=='o' and game_board[2]=='o')\
         or (game_board[0]=='o' and game_board[4]=='o' and game_board[8]=='o')\
         or (game_board[0]=='o' and game_board[3]=='o' and game_board[6]=='o')\
         or (game_board[2]=='o' and game_board[5]=='o' and game_board[8]=='o')\
         or (game_board[3]=='o' and game_board[4]=='o' and game_board[5]=='o')\
         or (game_board[6]=='o' and game_board[7]=='o' and game_board[8]=='o')\
         or (game_board[6]=='o' and game_board[4]=='o' and game_board[2]=='o')\
         or (game_board[1]=='o' and game_board[4]=='o' and game_board[7]=='o'):
        return 'o'
 
def draw():#Function to check if the game is a draw
    '''
    Checks if game is a draw

    Function that checks if all spots are taken and the checkwin() condition isn't satisfied therefore it's a draw.

    :returns: a draw if conditions are satisfied
    '''
    
    if (checkwin()!= 'x' or checkwin()!='o')\
        and ( (game_board[0]=='o' or game_board[0]=='x') and (game_board[1]=='o' or game_board[1]=='x')\
        and (game_board[2]=='o' or game_board[2]=='x') and (game_board[3]=='o' or game_board[3]=='x')\
        and (game_board[4]=='o' or game_board[4]=='x') and (game_board[5]=='o' or game_board[5]=='x')\
        and (game_board[6]=='o' or game_board[6]=='x') and (game_board[7]=='o' or game_board[7]=='x')\
        and (game_board[8]=='o' or game_board[8]=='x')):
        return ('draw')

def save():#Saves the game
    '''
    Saves game

    This function saves the game in bytes using the pickle function
    
    '''
    global game_board
    f=open("savegame.txt","wb")
    pickle.dump(game_board,f)
    f.close()

def load():#Loads the game
    '''
    Loads the game
    
    This function loads the game after the game gets saved
    '''
    global game_board
    f=open("savegame.txt","rb")
    d=pickle.load(f)
    game_board=d
    f.close()

    
game_over=False
def play():#One player game
    '''
    Function for the one player game

    This is the code for the one player game i.e. the players moves.
    Checkwin(), Draw(),board(), save() and load() are called in this function
    
    '''
    global game_over
    while game_over==False:#Checks if the number input is within range and plays the number chosen
        
        user_choice=int(input('Please enter a number. Enter 500 to save a game. ' ))
        if user_choice == 500:
            save()
            print("Game saved.")
            break
        elif (user_choice<0 or user_choice>8) or game_board[user_choice]!=user_choice :
            print("That's out of range or already taken " )
            user_choice=int(input('Please enter a number ' ))
            game_board[user_choice]='x'
            
        else:
            game_board[user_choice]='x'#x moves
            
        if checkwin()=='x':#Checks if X won
            print ('x wins')
            game_over = True
            board()
            break#Breaks code if x wins
        
        if draw()=='draw':#Checks if draw after player 1's move
            print ("it's a draw")
            break #Breaks code if draw    

            
        while True:
            
            computer_choice=random.randint(0,8)#Computer makes a random move

            if game_board[computer_choice]!='o' and game_board[computer_choice]!='x':#Checks whether the spot is taken
                game_board[computer_choice]='o'
                board()
                break
                
        if checkwin()=='o':#Checks if o won
            print ('o wins')
            game_over = True
            board()
            
            break #Breaks code if o wins
        if draw()=='draw':#Checks if draw after player computer moves
            print ("it's a draw")
            break #Breaks code if draw    
                
            board()
        
            
game_over = False

def two_player(): #2 player game
    
    '''
    Function for the two player game

    2 player game in which X starts and O plays second. 

    Checkwin(),draw() and board() are called in this function.
    '''
    
    global game_over
    while not game_over:
        user_choice1=int(input('Please enter a number ' ))
        #Checks if input is within bounds and that the spot isn't taken
        if (user_choice1<0 or user_choice1>8) or game_board[user_choice1]!=user_choice1 :
                print("That's out of range or already taken " )
                user_choice1=int(input('Please enter a number ' ))
                game_board[user_choice1]='x'
        else:
            game_board[user_choice1]='x'#x moves
        
        if checkwin()=='x':#Checks if X won
            print ('x wins')
            game_over = True
            board()
            break
        
        if draw()=='draw':#Checks if draw after player 1's move
            print ("it's a draw")
            break #Breaks code if draw
        
        board()
        
        user_choice2=int(input('Please enter a number ' ))
        #Checks if input is within bounds and that the spot isn't taken

        if (user_choice2<0 or user_choice2>8) or game_board[user_choice2]!=user_choice2 :
                print("That's out of range or already taken " )
                user_choice2=int(input('Please enter a number ' ))
                game_board[user_choice2]='o'
        else:
            game_board[user_choice2]='o'#o moves
          
        if checkwin()=='o':#Checks if o won
            print ('o wins')
            game_over = True
            board()
            
            break #Breaks code if o wins
        
        if draw()=='draw':#Checks if draw after player 2's move
            print ("it's a draw")
            break #Breaks code if draw
        
        board()
        
         
    
menu_start()  
