n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    # print(" "* (n-i),end=" ")
    # print("x"* (2*i-1),end=" ")     
    # print("\n")
    # print('x'*i,end="")
    if(i==1 or i==n):
        print('x'*n,end="")
    else:
        print('x',end="")
        print(" "*(n-2),end="")
        print('x',end="")
    print("")