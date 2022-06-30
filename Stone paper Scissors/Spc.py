from tkinter import *
from PIL import Image,ImageTk
from random import randint
#main window
root = Tk()
root.title("Stone Paper Scissor")
root.configure(background="magenta")

#picture
stone_img = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\stn.png"))
paper_img = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\ppr.png"))
scissor_img = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\ssr.png"))
stone_img_comp = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\stn1.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\ppr1.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("D:\VS Code work space\python\ssr1.png"))

#insert picture
user_label = Label(root, image = scissor_img, bg="magenta")
comp_label = Label(root, image = scissor_img_comp, bg="magenta")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#score
pscore = Label(root,text=0,font=100,bg="magenta",fg="white")
cscore = Label(root,text=0,font=100,bg="magenta",fg="white")
cscore.grid(row=1, column=1)
pscore.grid(row=1, column=3)
#indicator
pind = Label(root,font=50,text="PLAYER",bg="magenta",fg="white").grid(row=0, column=3)
Cind = Label(root,font=50,text="COMPUTER",bg="magenta",fg="white").grid(row=0, column=1)

#messages
msg = Label(root, font=50, bg="magenta",fg="white")
msg.grid(row=3, column=2)

#update message
def updatemessage(x):
    msg['text']=x

#update user score 
def updateuserscore():
    score = int(pscore["text"])
    score+=1
    pscore["text"]=str(score)

def updatecompscore():
    score = int(cscore["text"])
    score+=1
    cscore["text"]=str(score)

#check winner
def checkwin(p,c):
    if p == c:
        updatemessage("TIE")
    elif p == "stone":
        if c == "paper":
            updatemessage("LOST")
            updatecompscore()
        else:
            updatemessage("WINNER")
            updateuserscore()
    elif p == "paper":
        if c == "scissor":
            updatemessage("LOST")
            updatecompscore()
        else:
            updatemessage("WINNER")
            updateuserscore()
    elif p == "scissor":
        if c == "stone":
            updatemessage("LOST")
            updatecompscore()
        else:
            updatemessage("WINNER")
            updateuserscore()
    else:
        pass
#update choices
choices = ["stone","paper","scissor"]
def updatechoice(x):
#for computer
    cchoice = choices[randint(0,2)]
    if cchoice == "stone":
        comp_label.configure(image=stone_img_comp)
    elif cchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user

    if x=="stone":
        user_label.configure(image=stone_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,cchoice)

#buttons
Stone = Button(root,width=20,height=2,text="STONE",bg="#FF3E4D",fg="white",command = lambda:updatechoice("stone")).grid(row=2, column=1)
Paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updatechoice("paper")).grid(row=2, column=2)
Scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command = lambda:updatechoice("scissor")).grid(row=2, column=3)



root.mainloop()
