def factorial(num):
        if(num==1 or num==0):
            return 1
        return num*factorial(num-1)
    
num=int(input("Enter the number whose factorial is to be found:"))
print("factorial is:",factorial(num))