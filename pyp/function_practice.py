
#greatest of three

def greatest():
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=int(input("Enter a number:"))
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    else:
        return c
result=greatest()
print(result)

#degree c to f

def temp():
    t=int(input("Enter the temperature in degree c:"))
    return (t*9/5)+32
result=temp()
print("temp in farhenite is:",result,"degree f")

# sum of n natural numbers

def sum(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+sum(n-1)
n=int(input("Enter the number:"))
print("sum of natural numbers is",sum(n))

#pattern printing

def pattern():
    n=int(input("Enter the value of n:"))
    while(n>0):
        print('x'*n)
        n-=1
result=pattern()
print(result)