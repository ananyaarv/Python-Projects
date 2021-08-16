# NAME: Ananya Arvind
# DATE: 6/8/2021
# PERIOD: 8
# ACTIVITY: Final Project

board = [
[" " , " " , " "],
[" " , " " , " "],
[" " , " " , " "]
] 

# FUNCTIONS

# NAME: print_gameboard(gameboard)
# PURPOSE: to print the gameboard
# INPUT: none
# OUTPUT: displays 3x3 square gameboard 
def print_gameboard(gameboard):
  print(gameboard[0][0] + " | " + gameboard[0][1] + " | " + gameboard[0][2])
  print("---------")
  print(gameboard[1][0] + " | " + gameboard[1][1] + " | " + gameboard[1][2])
  print("---------")
  print(gameboard[2][0] + " | " + gameboard[2][1] + " | " + gameboard[2][2])

# NAME: check_winner(gameboard)
# PURPOSE: uses gameboard to check if player has won or not
# INPUT: none
# OUTPUT: 'X' or 'O' based on if either of the two players have won the game and a space character if neither player has won
def check_winner(gameboard):
  if gameboard[0][0] == "X" and gameboard[0][1] == "X" and gameboard[0][2]=="X": 
    return "X"
  if gameboard[0][0] == "O" and gameboard[0][1] == "O" and gameboard[0][2]=="O": 
    return "O"        
  if gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X":
    return "X"
  if gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O":
    return "O"  
  if gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X":
    return "X"  
  if gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O":
    return "O"  
  if gameboard[0][0] == "X" and gameboard[1][0] == "X" and gameboard[2][0] == "X":
    return "X"  
  if gameboard[0][0] == "O" and gameboard[1][0] == "O" and gameboard[2][0] == "O":
    return "O"  
  if gameboard[0][1] == "X" and gameboard[1][1] == "X" and gameboard[2][1] == "X":
    return "X"  
  if gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][1] == "O":
    return "O"  
  if gameboard[0][2] == "X" and gameboard[1][2] == "X" and gameboard[2][2] == "X":
    return "X"  
  if gameboard[0][2] == "O" and gameboard[1][2] == "O" and gameboard[2][2] == "O":
    return "O" 
  if gameboard[0][0] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X":
    return "X" 
  if gameboard[0][0] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O":
    return "O" 
  if gameboard[0][2] == "X" and gameboard[1][1] == "X" and gameboard[2][0] == "X":
    return "X" 
  if gameboard[0][2] == "O" and gameboard[1][1] == "O" and gameboard[2][0] == "O":
    return "O" 
  return " "  

# NAME: check_tied(gameboard)
# PURPOSE: to determine whether the game is tied (all 9 spaces are filled but no one has won)
# INPUT: none 
# OUTPUT: return True if tied (no empty spaces remaining) or return False if not tied 
def check_tied(gameboard):
  winner = check_winner(gameboard) 
  if winner == " ":
    return True
  else:
    return False

# NAME: make_move(gameboard, name, symbol)
# PURPOSE: to fill gameboard with current players move 
# INPUT: uses user's name for a row and a column 
# OUTPUT: places user symbol (X or O) in indicated spot on board
def make_move(gameboard, name, symbol):
  while True:
    row_number = input(str(name) + ", What row is your move? (Enter a number from 0 to 2)")
    column_number = input(str(name) + ", What column is your move? (Enter a number from 0 to 2)")
    row_number = int(row_number)
    column_number = int(column_number) 
    if row_number > 2 or column_number > 2 or row_number < 0 or column_number < 0:
      print("Invalid move, try again")
    elif gameboard[row_number][column_number] != " ":
      print("Invalid move, try again")
    else:
      gameboard[row_number][column_number] = symbol
      print_gameboard(gameboard) 
      break

# MAIN GAME LOOP
print("Welcome to tic-tac-toe, X's will go first\n")
playerX = input("What is the name of player X?")
playerO = input("What is the name of player O?")
i = 0
while (i<=9):
  make_move(board,playerX,"X") 
  i += 1  
  winner = check_winner(board)  
  if(winner != " "):
    print (playerX + " wins")
    break
  if(i==9):
    break  
  make_move(board,playerO,"O")
  i += 1
  winner = check_winner(board)  
  if(winner != " "):
    print (playerO + " wins")
    break
  
tied = check_tied(board)
if tied == True:
  print("Tie Game") 
