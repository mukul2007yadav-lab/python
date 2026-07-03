import random
computer=random.choice([0,1,-1])
print('''.        S for snakes
         G for gun
         W for water
                        ''')
str=input("Enter your choice:").upper()

choice={"S":1,"G":0,"W":-1}
reversechoice={1:"Snakes",0:"Gun",-1:"Water"}

you=choice[str]

print(f"You choose {reversechoice[you]}")
print(f"Computer choose {reversechoice[computer]}")

if(computer==str):
    print("Game draw!! try again")
else:
    if(computer==-1 and you==0):
        print("you loose!!")
    elif(computer==-1 and you==1):
        print("you win!!")
    elif(computer==1 and you==0):
        print("you win!!")
    elif(computer==1 and you==-1):
        print("you loose!!")
    elif(computer==0 and you==1):
        print("you loose!!")
    elif(computer==0 and you==-1):
        print("you win!!")
    else:
        print("Something went wrong!!")