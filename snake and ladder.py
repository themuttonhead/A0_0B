#snake_and_ladder
import random
count=0
while int(count<=100):
    i=input("press r to roll ")
    if i=="r":
        a=random.randint(1,6)
        count=count+a
        print("random number is",a)
        print("your position is",count)
        if count==8:
            count=37
            print("you may climb the ladder to",count)
           
        elif count==13:
            count=34
            print("you may climb the ladder to",count)
         
        elif count==40:
            count=68
            print("you may climb the ladder to",count)
            
        elif count==52:
            count=81
            print("you may climb the ladder to",count)
        
        elif count==76:
            count=97
            print("you may climb the ladder to",count)
         
        elif count==11:
            count=2
            print("you may go down as the snake ate you to",count)
            
        elif count==25:
            count=4
            print("you may go down as the snake ate you to",count)
           
        elif count==38:
            count=9
            print("you may go down as the snake ate you to",count)
          
        elif count==65:
            count=46
            print("you may go down as the snake ate you to",count)
           
        elif count==89:
            count=70
            print("you may go down as the snake ate you to",count)
            
        elif count==93:
            count=64
            print("you may go down as the snake ate you to",count)
           
        elif count+a>=100:
            print("you win")
      
    
    


    
