import numpy as np 
import random

x = input("Do you want to go first or second?")

    #if x == "first":
    
hand = np.array([['','',''],['','',''],['','','']])

#cnt = np.count_nonzero(x == "X")
#print(cnt)

cnt_row = np.count_nonzero(hand == "X", axis = 1) #counts xs in rows

cnt_col = np.count_nonzero(hand == "X", axis = 0) #counts xs in cols
while board[r,c] == "X" or "O":
    #get r, c again
if (cnt_col == 3 or cnt_row == 3):
    print("User Wins!")
else:
    print('Computer Wins!')

#create empty board [[____]]

#initialize boolean














