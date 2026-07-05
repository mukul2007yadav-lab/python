try:
    num=int(input("Enter your year of birth:"))
    print(num)

except Exception as e:
    print("Enter valid year of birth!!")

finally: # ye chlega hi chalega and this is basically used in functions when it returns after a particular task 
           # but a certain code blocl is still need to be executed thts where we use finally.
    print("Thank you!!")