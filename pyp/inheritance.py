class employee():
    company="microsoft"
    name="default"
    salary="xyz"
    def info(self):
        print(f"The name of employee is {self.name} and salary of emplyee is {self.salary}")

class coder:
    lang="python"
    def printlang(self):
        print(f"your language is {self.lang}")


class programer(employee,coder):
    company="google"  
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.lang}")      
a=employee()
b=programer()
b.showlanguage()