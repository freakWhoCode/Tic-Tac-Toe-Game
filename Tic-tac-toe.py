
from tkinter import*

import random

 

#For restarting the Game

def restart():

    for i in range(3):

        for j in range(3):

            buttons[i][j].config(text="")

 

    player=random.choice(players)

    label.config(text=player +" Player's move")

 

#For checking Winner

def check_winner():

    #Row Checking

    for i in range(3):

        if buttons[i][0]['text']==buttons[i][1]['text']==buttons[i][2]['text']!="":

            buttons[i][0].config(bg="pink")

            buttons[i][1].config(bg="pink")

            buttons[i][2].config(bg="pink")

            return True

       

    #Column checking

    for i in range(3):

        if buttons[0][i]['text']==buttons[1][i]['text']==buttons[2][i]['text']!="":

            buttons[0][i].config(bg="pink")

            buttons[1][i].config(bg="pink")

            buttons[2][i].config(bg="pink")

            return True

 

    #Diagonal Checking

 

    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":

        buttons[0][0].config(bg="pink")

        buttons[1][1].config(bg="pink")

        buttons[2][2].config(bg="pink")

        return True

 

    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":

        buttons[0][0].config(bg="pink")

        buttons[1][1].config(bg="pink")

        buttons[2][2].config(bg="pink")

        return True

    else:

        return False

 

#To check whether the game is tied or not

def Tie():

    counter=0

    for i in range(3):

        for j in range(3):

            if  buttons[i][j]['text']=="":

                counter=counter+1

               

    if counter==0:

        return True

    else:

         return False

 

#For the next Player's Move

def move(row,column):

    global player

 

    if buttons[row][column]['text']=="" and check_winner() is False:

        if player==players[0]:

            buttons[row][column]['text']=player

            if check_winner() is True:

                label.config(text=player + " Won The Game")

            elif Tie() is True:

                label.config(text="Game Tied")

            else:

                label.config(text=players[1]+" player's move")

                player=players[1]

        else:

            buttons[row][column]['text']=player

            if check_winner() is True:

                label.config(text=player + " Won The Game")

            elif Tie() is True:

                label.config(text="Game Tied")

           

            else:

                label.config(text=players[0]+" player's move")

                player=players[0]

       

#User Interface Design

root=Tk()

 

buttons=[[0,0,0],[0,0,0],[0,0,0]]

 

players=["X","O"]

player=random.choice(players)

 

label=Label(root,text=player +" Player's Move",fon=("comic sans ms",20,"bold"),fg="orange")

label.pack()

 

#Frame to use grid functionality

 

frame=Frame(root)

frame.pack()

 

#Creation of Buttons and Gridded them together

for i in range(3):

    for j in range(3):

        buttons[i][j]=Button(frame,text="",fg="black",bg="light blue",width=12,height=5,command=lambda i=i,j=j:move(i,j),font=("Comic sans ms",13,"bold"))

        buttons[i][j].grid(row=i,column=j)

 

#To Restart the Game

 

res_button=Button(root,text="Restart",command=restart,fg="black",bg="white",font=("comic sans ms",15,"bold"))

res_button.pack(side=RIGHT)

 

root.title("Tic-Tac-Toe by 09xUnique")

root.mainloop()

 

 

 



 

