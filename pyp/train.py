import random
class train():

    def __init__(self,TrainNo):
        self.TrainNo=TrainNo

    def bookstatus(self,fro,to):
        print(f"Train wiht Train number {self.TrainNo} is booked from {fro} to {to}")

    def fare(self,fro,to):
        print(f"Train wiht Train number {self.TrainNo} is booked from {fro} to {to} having fare  {random.randint(500,5000)}" )

    def runningstatus(self):
        print(f"Train with train nuber {self.TrainNo} is running on time")
        
t=train(22222)
t.bookstatus("Delhi","Csmt")
t.fare("Delhi","Csmt")
t.runningstatus()
