#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, FR, To):
        print(f"Ticket is booked, train no is: {self.trainNo}\nfrom: {FR} to: {To}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time.")

    def getFare(self, FR, To):
        print(f"Train no: {self.trainNo}\nfrom: {FR} to: {To}\nThe fare is: {randint(111,7777)}")

t = Train(223452)
t.book("Kolkata", "Delhi")
t.getStatus()
t.getFare("Kolkata", "Delhi")
