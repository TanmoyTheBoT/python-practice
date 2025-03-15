# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint

class Train:
    # def __init__(self , trainName , trainNo , availableSeats, fare):
    def __init__(self , trainName , trainNo):
        self.trainName = trainName
        self.trainNo = trainNo
        # self.availableSeats = availableSeats
        # self.fare = fare


    def book(self , fro, to, numTickets):
        if numTickets <= availableSeats:
            print(f"{numTickets} Ticket(s) is book in {self.trainName} , train no is {self.trainNo} from {fro} to {to}")

        else:
            print("Not enough seats available!")

    
    def getStatus(self):
        print(f"The Train Name is {self.trainName} and train no is {self.trainNo} and currently available seats {availableSeats}")
        # print(f"The Train Name is {self.trainName} and train no is {self.trainNo} and currently available seats {self.availableSeats}")

    def getFare(self, fro, to, numTickets):
        print(f"The Ticket Fare for {self.trainName} and train no is {self.trainNo} form {fro} to {to} is {fare*numTickets} ")
        # print(f"The Ticket Fare for {self.trainName} and train no is {self.trainNo} form {fro} to {to} is {self.fare*numTickets} ")

# Initialize availableSeats and fare using randint, then create a Train object.

availableSeats = randint(10, 20)
fare = randint(100, 200)

# t = Train(trainName="Rangpur Express", trainNo=767, availableSeats=886, fare=999 )
t = Train(trainName="Rangpur Express", trainNo=767, )
t.book(fro="Rangpur", to="Dhaka", numTickets=20)
t.getStatus()
t.getFare(fro="Rangpur", to="Dhaka", numTickets=1)
