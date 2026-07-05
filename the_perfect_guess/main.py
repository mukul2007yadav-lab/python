import random

def guess_number():
    cpnum=random.randint(0,100)
    num=None
    chance=1
    while(cpnum!=num):
        num=int(input("Enter your number :"))
        if(cpnum>num):
                print("higher number please!!")
        elif(cpnum<num):
                print("Lowe number please!!")
        else:
            print(f"you took {chance} chances to guess the correct number ")
            print(f"your number is {num} and computer's was also {cpnum}")
        chance+=1
            
 
guess_number()