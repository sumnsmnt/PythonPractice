# Can you change the self-parameter inside a class to something else (say "suman"). 
# Try changing self to “slf” or "suman" and see the effects.

#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(suman, FR, To):
        print(f"Ticket is booked, train no is: {suman.trainNo}\nfrom: {FR} to: {To}")

    def getStatus(anything):
        print(f"Train no {anything.trainNo} is running on time.")

    def getFare(anything_else, FR, To):
        print(f"Train no: {anything_else.trainNo}\nfrom: {FR} to: {To}\nThe fare is: {randint(111,7777)}")

t = Train(223452)
t.book("Kolkata", "Delhi")
t.getStatus()
t.getFare("Kolkata", "Delhi")
