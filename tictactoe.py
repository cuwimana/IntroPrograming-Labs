# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Charlotte Uwimana
# Created: 2017-10-27
symbol = [ " ", "x", "o" ]
def printRow(row):
    output = "|"  # initialize output to the left border
    for square in row: # for each square in the row...
	# add to output the symbol for this square followed by a border 
        output += " " + symbol[square] + " |"
        print(output)# print the completed output for this row
def printBoard(board):
    print("+---------+")# print the top border
    for row in board:# for each row in the board...	
        printRow(row) # print the row	
        print("+---------+") # print the next border
def markBoard(board, row, col, player):
    if board[row][col] == 0:# check to see whether the desired square is blank
        board[row][col] = player # if so, set it to the player number
def getPlayerMove():
    row = int(input(" Enter number of rows: "))
    col = int(input (" Enter number of columns: ")) # prompt the user separately for the row and column numbers
    return (row,col) # then return that row and column instead of (0,0)
def hasBlanks(board):
    for row in board: # for each row in the board...
        for square in row: # for each square in the row...
            if square == 0:# check whether the square is blank
                return True # if so, return True
            else:
                return True # if no square is blank, return False
def main():
    board = [ [0,0,0]
            , [0,0,0]
            , [0,0,0] ] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        success = markBoard(board,row,col,player)
	#the check if success before switching turns
        player = player % 2 + 1 # switch player for next turn
main()
