f=open("text.txt")
data=f.read()
print(data)
f.close()

str=input("Enter the message you want to be saved:")
file=open("message.txt","w")
file.write(str)
file.close()
