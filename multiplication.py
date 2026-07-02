num=int(input("Enter the number whose table you want:"))
for i in range(1,11):           # via for loop
    print(num,"*",i,"=",(num*i))
i=1
while(i<=10):
    print(num,"*",i,"=",(num*i))# via while loop
    i+=1
i=10.    #table in revrse via while loop
while(i>0):
    print(num,"x",i,"=",(num*i))
    i-=1