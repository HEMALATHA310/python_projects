'''
Created on 17-Sep-2021

@author: hemalatha
'''
#TIC_TAC_TOE PROGRAM USING RANDOM IN PYTHON

from time import sleep

'''import necessary libraries'''
import numpy as np
import random

'''create a empty play board'''
def create_newboard():#function definiton
    return (np.array([[0,0,0],[0,0,0],[0,0,0]]))
'check for empty place'
def space(board):
    l=[]#empty list
    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[i][j]==0:
                l.append((i,j))
    return(l)  
'Select random place for player'
def ran_place(board,player):
#     current_loc=random.choice(space(board))
#     print(current_loc)
    selection=space(board)
    current_loc=random.choice(selection)
    board[current_loc]=player
    return(board)
'horizontal row check'
def row_win(board,player):
    for x in range(len(board)):
        win=True
        
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
            if win == True:
                return(win)
    return(win)
'vertical check'
def col_win(player,board):
    for x in range(len(board)):
        win=True
        
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
            if win == True:
                return(win)
    return(win)
'diagnol check'
def diag_win(board,player):
    win=True
    y=0
    for x in range(len(board)):
        if board[x,x]!=player:
            win=False
    if win:
        return win
    
    win=True
    if win:
        for x in range(len(board)):
            y=len(board)-1-x
            if board[x,y]!=player:
                win=False
            
    return(win)
'evaluate winner or tie'
def evaluate(board):
    winner=0
    
    for player in [1,2]:
        if (row_win(board,player) or col_win(board,player) #condition check
            or diag_win(board,player)):
            
            winner=player
        
        if np.all(board!=0)and winner==0:
            winner=-1
        return winner
    
'main function'
def play():
    board,winner,counter=create_newboard(),0,1 #empty board func call
    print(board)
    sleep(2)
    
    while winner == 0:
        for player in [1,2]:
            board=ran_place(board,player)
            print('board after'+ str(counter)+'move')
            print(board)
            sleep(2)
            counter+=1
            winner=evaluate(board)
            if winner!=0:
                break
            
    return (winner)
'drive code'
print("winner is:", str(play()))        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
       
            


       
         
            
                       
            
                       
