from tkinter import *
from PIL import Image, ImageTk
from random import randint



screen = Tk()
screen.title("ROCK PAPER AND SCISSOR GAME")
screen.geometry("800x600")
screen.configure(background="grey")

#include images

pic_rock1 = ImageTk.PhotoImage(Image.open("rock2.png"))
pic_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png"))
pic_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
pic_rock2 = ImageTk.PhotoImage(Image.open("rock2.png"))
pic_scissor2 = ImageTk.PhotoImage(Image.open("scissor1.png"))
pic_paper2 = ImageTk.PhotoImage(Image.open("paper1.png"))


label_player = Label(screen, image=pic_scissor1)
label_computer = Label(screen,image=pic_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)


# scores
c_score = Label(screen, text=0, font=("Sans serif", 40,"bold"),fg="blue")
p_score = Label(screen, text=0, font=("Sans serif", 40,"bold"),fg="blue")

c_score.grid(row=1, column=1)
p_score.grid(row=1, column=3)

# COMPUTER AND PLAYER SCORES
p_indicator = Label(screen,font=("Sans serif", 20, "bold"), text="PLAYER",
                    bg="MediumSpringGreen", fg="Olive")

c_indicator = Label(screen,font=("Sans serif", 20, "bold"), text="COMPUTER",
                    bg="MediumSpringGreen", fg="Olive")
c_indicator.grid(row=0, column=1)
p_indicator.grid(row=0, column=3)


def msg_updation(x):
    last_msg["text"] = x


def computer_update():
    last = int(c_score["text"])
    last+=1
    c_score["text"] = str(last)


def player_update():
    last = int(p_score["text"])
    last += 1
    p_score["text"] = str(last)


def check_winner(player, computer):
    if player == computer:
        msg_updation("It's a draw")
    elif player == "rock":
        if computer == "paper":
            msg_updation("Rock is defeated by Paper. You lose!")
            computer_update()
        else:
            msg_updation("Paper beats Rock. You win!")
            player_update()
    elif player == "paper":
        if computer == "scissor":
            msg_updation("Paper is defeated by Scissors. You lose!")
            computer_update()
        else:
            msg_updation("Scissors beats Paper. You win!")
            player_update()
    elif player == "scissor":
        if computer == "rock":
            msg_updation("Rock beats scissor.You lose!")
            computer_update()
        else:
            msg_updation("You Win!")
            player_update()
    else:
        pass

to_select = ["rock", "paper", "scissor"]
def update_choice(x ):
    computer_choice = to_select[randint(0,2)]
    if computer_choice == "rock":
        label_computer.configure(image=pic_rock2)
    elif computer_choice == "paper":
        label_computer.configure(image=pic_paper1)
    else:
        label_computer.configure(image=pic_scissor2)
    if x== "rock":
        label_player.configure(image=pic_rock1)
    elif x== "paper":
        label_player.configure(image=pic_paper1)
    else:
        label_player.configure(image=pic_scissor1)
    check_winner(x, computer_choice)




last_msg = Label(screen, font=("Typography", 40, "bold"), bg="LightSalmon", fg="HotPink")
last_msg.grid(row=3, column=2, columnspan=2)  # Add columnspan to occupy two columns

# Def the rock,paper ,scissor button

b_rock = Button(screen, width=15, height=3, text="ROCK",
       font=("Sans serif", 18, "bold"), bg="maroon",
       fg="hot pink", command=lambda: update_choice("rock")).grid(row=2, column=1)

b_paper = Button(screen, width=15, height=3, text="PAPER",
       font=("Sans serif", 18, "bold"), bg="maroon",
       fg="hot pink", command=lambda: update_choice("paper")).grid(row=2, column=2)

b_scissor = Button(screen, width=15, height=3, text="SCISSOR",
       font=("Sans serif", 18, "bold"), bg="maroon",
       fg="hot pink", command=lambda: update_choice("scissor")).grid(row=2, column=3)


screen.mainloop()


# Paper is defeated by Scissors. You lose!