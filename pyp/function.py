def avg():# function definition
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=int(input("Enter a number:"))

    average=(a+b+c)/3
    print(average)
    print("see you soon")
n=int(input("Enter number of times you want average of 3 sums:"))
for i in range(n):
    avg()#function call