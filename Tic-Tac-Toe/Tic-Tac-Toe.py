# Tic-Tac-Toe

import random    

# Draw a Game Area 
data = [] # <class 'list'>

def new_game(): # Print empty area  
    A =''
    for i in range(3): # Row
        for j in range(6): # Column
            
            if j%2 == 0: # _
                data.append('_')
                A += '_'
            
            elif j == 5: # new line
                A += '\n'
                
            else: # |
                A += '|'
    print(A)
new_game()
# _|_|_\n
# _|_|_\n
# _|_|_\n
    
# Player 1 : (X)
def player_1():
    while True:        
        print("\nplayer 1 : (X)")
        while True:
            ply_1 = int(input("Choose a position from (1-9) : ")) # player 1
            if ply_1>0 and ply_1<10:
                break
            
        
        if data[(ply_1)-1] == '_': # !! Control !!
            
            data[(ply_1)-1] = 'X' # Value is changed
                                  # new value is X
            
            A = '' 
            counter = 0
            
            # Update
            for i in range(3): # Row
                for j in range(6): # Column
                    
                    if j%2 == 0: # '_'
            
                        if(counter == ply_1-1):
                            A += "X"
                            counter += 1
                        else:
                            A += data[counter] # Same value
                            counter += 1
                    
                    elif j == 5: # new line
                        A += '\n'
                    
                    else: # '|'
                        A += '|'
            print(A) # Show  
            break
         
        else:
            print("You can't go there")

def player_2():
  
    while True:
        
        print("\nplayer 2 : (Y)")   
        # Random number
        ply_2 = random.randint(1,9) 
        print(f"Player 2 : {ply_2}")
        
        # Real person
        #ply_2 = int(input("Choose a position from (1-9) : ")) # player 2
        
        if data[(ply_2)-1] == '_': # !! Control !!
             
            data[(ply_2)-1] = 'O'# Value is changed
                                 # new value is X
            
            A = ''
            counter = 0
            
            for i in range(3): # Row
                for j in range(6): # Column
                    
                    if j%2 == 0: # '_'
            
                        if(counter == ply_2-1):
                            A += "O"
                            counter += 1
                        else:
                            A += data[counter]  
                            counter += 1
                    
                    elif j == 5: # new line
                        A += '\n'
                    
                    else: # '|'
                        A += '|'
            print(A)
            break
        else:
            print("You can't go there")
            
# Check  _ _ _

#  -> 0 1 2
#  -> 3 4 5
#  -> 6 7 8
def check():    # Row conrol 
    res = 0
    for i in range(9): 
        if ((i==0)or(i==3)or(i==6)):
            if(data[i] == 'X'): # X control X X X
                for j in range(3):
                   if(data[i+j] == 'X'):
                       res += 1
                       if res == 3:
                           return 'X'
                   else:
                       res = 0
                       break
            if(data[i] == 'O'): # O control O O O
                for j in range(3):
                   if(data[i+j] == 'O'):
                       res += 1
                       if res == 3:
                           return 'O' 
                   else:
                       res = 0
                       break
    # Reverse Contol 
    res = 0             
    for i in range(9): 
        if ((i==2)or(i==5)or(i==8)):
            if(data[i] == 'X'):
                for j in range(3):
                   if(data[i-j] == 'X'):  # X control X X X
                       res += 1
                       if res == 3:
                           return 'X'
                   else:
                       res = 0
                       break
            if(data[i] == 'O'):  # O control O O O
                for j in range(3):
                   if(data[i-j] == 'O'):
                       res += 1
                       if res == 3:
                           return 'O' 
                   else:
                       res = 0
                       break                      
    
#  | | | 
#  0 1 2
#  3 4 5
#  6 7 8
def check_2(): # Column control
    res = 0
    for i in range(9): 
        if ((i==0)or(i==1)or(i==2)):
            if(data[i] == 'X'): # X control X X X
                for j in range(i,8,3):
                   if(data[j] == 'X'):
                       res += 1
                       if res == 3:
                           return 'X'
                   else:
                       res = 0
                       break
            if(data[i] == 'O'): # O control O O O 
                for j in range(i,8,3):
                   if(data[j] == 'O'):
                       res += 1
                       if res == 3:
                           return 'O' 
                   else:
                       res = 0
                       break
    # Reverse
    res = 0
    for i in range(9): 
        if ((i==6)or(i==7)or(i==8)):
            if(data[i] == 'X'): # X control X X X
                for j in range(i,-1,-3):
                   if(data[j] == 'X'):
                       res += 1
                       if res == 3:
                           return 'X'
                   else:
                       res = 0
                       break
            if(data[i] == 'O'): # O control O O O 
                for j in range(i,-1,-3):
                   if(data[j] == 'O'):
                       res += 1
                       if res == 3:
                           return 'O' 
                   else:
                       res = 0
                       break
     

def diagon(): # Diagonal control 
    res = 0
    for i in range(9): 
        if ((i==0)or(i==2)):
            if(data[i] == 'X'): # X control X X X
                # \
                if i == 0: 
                    for j in range(i,9,4):
                        if(data[j] == 'X'):
                            res += 1
                            if res == 3:
                                return 'X'
                        else:
                            res = 0
                            break
                # /
                else:
                    for j in range(i,8,2):
                        if(data[j] == 'X'):
                            res += 1
                            if res == 3:
                                return 'X'
                        else:
                            res = 0
                            break
                    
            if(data[i] == 'O'): # O control O O O
                # \ 
                if i == 0:
                    for j in range(i,9,4):
                        if(data[j] == 'O'):
                            res += 1
                            if res == 3:
                                return 'O'
                        else:
                            res = 0
                            break
                # /   
                else:
                    for j in range(i,8,2):
                        if(data[j] == 'O'):
                            res += 1
                            if res == 3:
                                return 'O'
                        else:
                            res = 0
                            break
                    

def Res(winner): # Show Winner
     if winner == 'X':
        print("Player 1 is Winner")
        return 'A'
     elif winner == 'O':
        print("Player 2 is Winner")
        return 'B'

def Menu():
    print("\n1.) New Game ")
    print("2.) Quit")
    
    while True:
        ex = int(input("Please enter process number : "))
        if (ex == 1) or (ex == 2):
            return ex
            break

# Main Function
counter = 0
while True:
    
    player_1()
    counter += 1
    winner = check()
    if Res(winner) == 'A':
        ng = Menu() # Menu Part
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
    winner_2 = check_2()
    if Res(winner_2) == 'A':
        ng = Menu() # Menu Part
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
        
    winner_3 = diagon()
    if Res(winner_3) == 'A':
        ng = Menu() # Menu Part
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
    if counter == 9:
        print("Draw")
        ng = Menu()
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
    
    player_2()
    counter += 1
    winner = check()
    if Res(winner) == 'B':
        ng = Menu()
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
        
    winner_2 = check_2()
    if Res(winner_2) == 'B':
        ng = Menu()
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
    winner_3 = diagon()
    if Res(winner_3) == 'B':
        ng = Menu()
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
    if counter == 9:
        print("Draw")
        ng = Menu()
        if ng == 1:
            data = []
            counter = 0
            ch1 = 0
            new_game()
        elif ng == 2:
            break
    
