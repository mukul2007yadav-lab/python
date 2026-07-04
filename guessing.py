import random
def game():
    print("You are playing a game:")
    score=random.randint(1,100)
    f=open("hiscore.txt","r+")
    content=f.read()
    f.close()
    if content=="":
        hiscore=0
    else:
        hiscore=int(content)
    
    print(f"your score is {score}")
    if(score>hiscore ):
        f.open("hiscore.txt","w")
        f.write(str(score))
        f.close()
    return score
    
game()