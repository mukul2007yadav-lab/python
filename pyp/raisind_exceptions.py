a=int(input("Enter a nmber:"))
b=int(input("Enter second nmber:"))

if b==0:
    raise ZeroDivisionError("second number cant be zero")

else:
    print(f" the division a/b is {a/b}")