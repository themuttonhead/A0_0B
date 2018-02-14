#Rock_paper_program
import random
l=["rock","paper","scissor"]
i=input("press y to play ")
while(i=="y"):
    a=input("choose r:for rock, p:for paper or s:for scissor ")
    b=random.choice(l)
    print("computer chose",b)
    print("your choice is",a)
    if a=="r":
        if b==l[0]:
            print("its a tie")
        elif b==l[1]:           
            print("computer wins")
        elif b==l[2]:           
            print("you win")
    elif a=="p":
        if b==l[1]:           
            print("its a tie")
        elif b==l[2]:           
            print("computer wins")
        elif b==l[0]:
            print("you win")
    elif a=="s":
        if b==l[2]:           
            print("its a tie")
        elif b==l[0]:            
            print("computer wins")
        elif b==l[1]:            
            print("you win")
    else:
        print("please choose")
    c=input("press q to quit and p to play ")
    if c=="q":
        print("thank you")
        break
    elif c=="p":
        print("continue the game")
        
