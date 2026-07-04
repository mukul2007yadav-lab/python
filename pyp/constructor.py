class employee():
    lang="Python,Java,C++,HTML,CSS,Java script" #class attributes
    salary=2400000

    def __init__(self,name,lang,salary):# dunder method
        self.name=name
        self.salary=salary
        self.lang=lang
        print("Namashakar")

    def getInfo(self):#self parameter
        print(f"The language is {self.lang}. The salary is {self.salary}")
    
    @staticmethod       #static method
    def greeting():
        print("Good morning!!")

ashu=employee("Mukul","x",2000000)
print(ashu.name,ashu.lang,ashu.salary)
Ishu=employee("Mayank","Hindi",2500000)
print(Ishu.name,Ishu.lang,Ishu.salary)

ashu.name="Mukul"     #instance attribute
ashu.greeting()
print(ashu.name)
ashu.getInfo()